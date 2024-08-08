"""
       _Write_eML of the eML system
   
           created by RD McCann on 7/28/2024
    Copyright (c) 2024 Turtle Bay Geophysical LLC
                ALL RIGHTS RESERVED.

 Questions and comments can be directed to: Support@TurtleBayGeophysical.com
                 
  Licensed under the Attribution-NonCommercial-ShareAlike 4.0 International 
  (CC BY-NC-SA 4.0) (the "License"); you may not use this file except in 
  compliance with the License.
  
  You may obtain a copy of the License at
 
      https://creativecommons.org/licenses/by-nc-sa/4.0/
 
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""
import os
from datetime import date, datetime

import numpy as np


class _Write_eML:  # ================================================================ Write_eML >>>v
  """
  Writes the eML file.
  valid data types that are used include the following:
    Primitives:
      bool, byte, int, float, complex, str, datetime, date
    Containers:
      dict, list, set, tuple, and FrozenSet
  """

  def __init__(self, eml_filename: str, eml_meta_data: dict,
               identifiers: dict, eml_data: dict):
    """
    converts the entries into the relative string equivalents and outputs the data to the eML file.

    :param eml_filename: the fully qualified eML filename
    :param eml_meta_data: the meta data of the eML file
    :param eml_data: the user specified data of the eML file
    """
    self.eml_filename = eml_filename

    # class variables
    # holds all of the eML lines createed through the user specified data. These will be output to
    # a file on close.
    self.eml_meta_data = eml_meta_data
    self.identifiers = identifiers
    self.eml_data = eml_data

    self.current_version = 0.10

    self.linesout = list()
    self.linesout.append('eML Header | ' + str(self.eml_meta_data['version']) + ' | '
                         + self.eml_meta_data['lamguage'] + ' | '
                         + self.eml_meta_data['creation date'].strftime(
      '%m/%d/%Y %H:%M:%S.%f') + ' | '
                         + self.eml_meta_data['last update'].strftime('%m/%d/%Y %H:%M:%S.%f'))

    for id, entrytype in identifiers.items():
      match entrytype:
        case 'array':
          self.setArray(id, self.eml_data[id])
        case 'bool':
          self.setBoolean(id, self.eml_data[id])
        case 'int':
          self.setInt(id, self.eml_data[id])
        case 'float':
          self.setFloat(id, self.eml_data[id])
        case 'complex':
          self.setComplex(id, self.eml_data[id])
        case 'string':
          self.setString(id, self.eml_data[id])
        case 'date':
          self.setDate(id, self.eml_data[id])
        case 'datetime':
          self.setDateTime(id, self.eml_data[id])
        case 'dict':
          self.setDict(id, self.eml_data[id])
        case 'list':
          self.setList(id, self.eml_data[id])
        case 'set':
          self.setSet(id, self.eml_data[id])
        case 'tuple':
          self.setTuple(id, self.eml_data[id])
        case _:
          raise Exception('Write error: invalid entry type ' + str(entrytype))
    pass

  def setArray(self, identifier, value: np.ndarray):  # ------------------------------- setArray >>
    """
    Converts an array to string for output to linesout.

    :param identifier: user defined identifier for this array
    :param value: the array to be output to a string
    """
    datatype = self._getArrayDataType(value)
    currline = identifier + ' := ' + '<array|' + datatype + '|' + str(value.shape) + '> '
    bufferlength = len(currline)

    farray = value.flatten()

    isfirst = True
    for item in farray:
      if not isfirst:
        currline = currline + '|'
      isfirst = False
      if datatype=='':
        currline = currline + self._appendPrimitive(item)
      else:
        currline = currline + str(item)

    self.linesout.append(currline)

    # currline = ' ' * bufferlength
    pass

  def setBoolean(self, identifier, value):  # -------------------------------- setBoolean >>
    """
    writes a boolean value to the eml file

    :param identifier: identifier for this boolean value
    :param value:  value to be written to the eml file
    """
    self.linesout.append(identifier + ' := ' + self._appendPrimitive(value))
    pass

  def setComplex(self, identifier, value):  # ----------------------------- setComplex >>
    """
    writes a complex value to the eml file

    :param identifier: identifier for this complex value
    :param value:  value to be written to the eml file
    """
    self.linesout.append(identifier + ' := ' + self._appendPrimitive(value))
    pass

  def setDate(self, identifier, value: date):  # -------------------------------- setDate >>
    """
    writes a date value to the eml file

    :param identifier: identifier for this date value
    :param value:  value to be written to the eml file
    """
    self.linesout.append(identifier + ' := ' + self._appendPrimitive(value))
    pass

  def setDateTime(self, identifier, value: datetime):  # -------------------------- setDateTime >>
    """
    writes a date time value to the eml file

    :param identifier: identifier for this date time value
    :param value:  value to be written to the eml file
    """
    self.linesout.append(identifier + ' := '
                         + self._appendPrimitive(value))
    pass

  def setDict(self, identifier, dictin: dict):  # -------------------------------------- setDict >>
    """
    Sets a dict to be output to an eML file.

    :param identifier: user specified string naming the dict for subsequent retrieval
    :param dictin: Input dict to be written to the eML file
    """
    currline = identifier + ' := <dict|' + str(len(dictin)) + '>'

    starting_line_length = len(currline)
    for key, value in dictin.items():
      # append the key/value data type if appropriate '
      currline = currline + self._appendPrimitive(key) + '|'

      if self._isPrimitive(value):
        # the current value is a primative, append it to the current line
        self.linesout.append(currline + self._appendPrimitive(value))
      else:
        self._appendContainer(currline, value)

      currline = ' ' * starting_line_length
      pass

  def setFloat(self, identifier, value):  # -------------------------------- setFloat >>
    """
    writes a float value to the eml file

    :param identifier: identifier for this float value
    :param value:  value to be written to the eml file
    """
    self.linesout.append(identifier + ':= ' + self._appendPrimitive(value))
    pass

  def setFrozenSet(self, identifier, value: frozenset):  # ----------------------- setFrozenSet >>
    """
    writes a frozenset value to the eml file

    :param identifier: identifier for this frozenset value
    :param value:  value to be written to the eml file
    """
    currline = identifier + ' := ' + '<frozenset|' + str(len(value)) + '> '
    bufferlength = len(currline)

    for item in value:
      if self._isPrimitive(item):
        self.linesout.append(currline + self._appendPrimitive(item))
      else:
        self._appendContainer(currline, item)

      currline = ' ' * bufferlength
    pass

  def setInt(self, identifier, value):  # -------------------------------- setInt >>
    """
    writes a int value to the eml file

    :param identifier: identifier for this int value
    :param value:  value to be written to the eml file
    """
    self.linesout.append(identifier + ' := ' + self._appendPrimitive(value))
    pass

  def setList(self, identifier, value: list):  # --------------------------------------- setList >>
    """
    Converts a list to string for output to linesout.

    :param identifier: user defined identifier for this set
    :param value: the list to be output to a string
    """
    currline = identifier + ' := ' + '<list|' + str(len(value)) + '> '
    bufferlength = len(currline)

    for item in value:
      if self._isPrimitive(item):
        self.linesout.append(currline + self._appendPrimitive(item))
      else:
        self._appendContainer(currline, item)

      currline = ' ' * bufferlength
    pass

  def setSet(self, identifier, value: set):  # ------------------------------------------ setSet >>
    """
    Converts a set to string for output to linesout.

    :param identifier: user defined identifier for this set
    :param value: the set to be output to a string
    """
    currline = identifier + ' := ' + '<set|' + str(len(value)) + '> '

    for item in value:
      if self._isPrimitive(item):
        self.linesout.append(currline + self._appendPrimitive(item))
      else:
        self._appendContainer(currline, item)

      currline = ' ' * len(currline)
      pass

  def setString(self, identifier, value):  # -------------------------------- setString >>
    """
    writes a string value to the eml file

    :param identifier: identifier for this string value
    :param value:  value to be written to the eml file
    """
    self.linesout.append(identifier + ' := ' + self._appendPrimitive(value))
    pass

  def setTuple(self, identifier, value: tuple):  # ------------------------------------ setTuple >>
    """
    Converts a tuple to string for output to linesout.

    :param identifier: user defined identifier for this tuple
    :param value: the tuple to be output to a string
    """
    currline = identifier + ' := ' + '<tuple|' + str(len(value)) + '> '

    for item in value:
      if self._isPrimitive(item):
        self.linesout.append(currline + self._appendPrimitive(item))
      else:
        self._appendContainer(currline, item)

      currline = ' ' * len(currline)
      pass

  def save(self):  # -------------------------------------------------------------------- save >>
    """
    saves the generated eml string to the file specified and closes the file
    """
    file = open(self.eml_filename, 'w')
    for nextline in self.linesout:
      file.write(nextline + "\n")
    file.close()
    pass

  def saveAs(self):  # ------------------------------------------------------------------ saveAs >>
    """
    Writes the generated eml string to the file specified and closes the file
    """
    if os.path.exists(self.eml_filename):
      raise Exception('eML save error: eml filename specified already exists, use saveAs instead')

    file = open(self.eml_filename, 'w')
    for nextline in self.linesout:
      file.write(nextline + "\n")
    file.close()
    pass

  def _appendContainer(self, currline, value):  # ----------------------------- _appendContainer >>
    """
    The input currline already has the key info assigned to it. Just need to append the new value.
    In this case the value is another container.

    :param currline: current line of text being created
    :param value: a container to be appended to the text file
    :return:
    """
    if isinstance(value, list):
      self._appendList2Existing(currline, value)
    elif isinstance(value, set):
      self._appendSet2Existing(currline, value)
    elif isinstance(value, dict):
      self._appendDict2Existing(currline, value)
    elif isinstance(value, tuple):
      self._appendTuple2Existing(currline, value)
    elif isinstance(value, frozenset):
      self._appendFrozenSet2Existing(currline, value)
    pass

  def _appendDict2Existing(self, currline: str, value: dict):  # --------- _appendDict2Existing >>
    """
    Appends a dict to an existing container element.

    :param currline: the current line being constructed for output
    :param value: the input list to be decomposed to strings
    """
    currline = currline + '<dict |' + str(len(value)) + '>'
    starting_currline_length = len(currline)

    for key, value in value.items():
      currline = currline + self._appendPrimitive(key) + '|'

      if self._isPrimitive(value):
        self.linesout.append(currline + self._appendPrimitive(value))
      else:
        self._appendContainer(currline, value)
      currline = ' ' * starting_currline_length
    pass

  def _appendDictKey(self, key):  # ---------------------------- _appendDictKey >>
    """
    Appends the value of key as a string to the current line.

    :param key: data value to be asppended
    :return: atring of the input key
    """
    lineout = ''

    # write the key to the current line, keys are primitives
    match self._getPrimitiveDataType(key):
      case 'bool':
        lineout += '<bool> ' + str(key)
      case 'int':
        lineout += '<int> ' + str(key)
      case 'float':
        lineout += '<float> ' + str(key)
      case 'complex':
        lineout += '<complex> ' + str(key)
      case 'str':
        lineout += '<str> ' + str(key)
      case 'datetime':
        lineout += '<datetime> ' + str(key)
      case 'date':
        lineout += '<date> ' + str(key)
      case _:
        raise Exception('Write eml error: Data type for ' + str(type(key))
                        + ' is not currently supported')

    return lineout
    pass

  def _appendFrozenSet2Existing(self, currline: str, value):  # ------ _appendFrozenSet2Existing >>
    """
    Appends a frozenset to an existing container element.

    :param currline: the current line being constructed for output
    :param value: the input frozenset to be decomposed to strings
    """
    currline = currline + '<frozenset |' + str(len(value)) + '>'
    bufferlength = len(currline)

    for item in value:
      if self._isPrimitive(item):
        self.linesout.append(currline + self._appendPrimitive(item))
      else:
        self._appendContainer(currline, item)
      currline = ' ' * bufferlength
    pass

  def _appendList2Existing(self, currline: str, value):  # ---------- _appendList2Existing >>
    """
    Appends a list to an existing container element.

    :param currline: the current line being constructed for output
    :param value: the input list to be decomposed to strings
    """
    currline = currline + '<list |' + str(len(value)) + '>'
    bufferlength = len(currline)

    for item in value:
      if self._isPrimitive(item):
        self.linesout.append(currline + self._appendPrimitive(item))
      else:
        self._appendContainer(currline, item)
      currline = ' ' * bufferlength
    pass

  def _appendPrimitive(self, value):  # --------------------------------------- _appendPrimitive >>
    """
    Writes a primative value to the current line and outputs it to linesout.

    :param value: value to be converted to string and output
    :return: string of the value to be output
    """
    match self._getPrimitiveDataType(value):
      case 'bool':
        return '<bool>' + str(value)
      case 'int':
        return '<int>' + str(value)
      case 'float':
        return '<float>' + str(value)
      case 'complex':
        return '<complex>' + str(value)
      case 'str':
        return '<str>' + str(value)
      case 'datetime':
        return '<datetime>' + value.strftime('%m/%d/%Y %H:%M:%S.%f')
      case 'date':
        return '<date>' + value.strftime('%m/%d/%Y')
      case _:
        raise Exception('Writeeml error: Data type for ' + str(type(value))
                        + ' is not currently supported')
    pass

  def _appendSet2Existing(self, currline: str, value: set):  # ------------- _appendSet2Existing >>
    """
    Appends a set to an existing container element.

    :param currline: the current line being constructed for output
    :param value: the input list to be decomposed to strings
    """
    currline = currline + '<set |' + str(len(value)) + '>'
    bufferlength = len(currline)

    isfirst = True
    for item in value:
      if self._isPrimitive(item):
        self.linesout.append(currline + self._appendPrimitive(item))
      else:
        self._appendContainer(currline, item)

      currline = ' ' * bufferlength
    pass

  def _appendTuple2Existing(self, currline: str, value: tuple):  # ------- _appendTuple2Existing >>
    """
    Appends a tuple to an existing container element.

    :param currline: the current line being constructed for output
    :param value: the input list to be decomposed to strings
    """
    currline = currline + '<tuple |' + str(len(value)) + '>'
    bufferlength = len(currline)

    for item in value:
      if self._isPrimitive(item):
        self.linesout.append(currline + self._appendPrimitive(item))
      else:
        self._appendContainer(currline, item)

      currline = ' ' * bufferlength
    pass

  def _getDataType(self, value):  # --------------------------------------------- _getDataType >>
    """
    returns the data type associated with the input value. Valid values are:
    bool, int, float, complex, str, date, datetime, list, set, and dict

    :param value: value to determine the data type of
    :return: the data type of the input value
    """
    if isinstance(value, bool):
      return 'bool'
    elif isinstance(value, int):
      return 'int'
    elif isinstance(value, float):
      return 'float'
    elif isinstance(value, complex):
      return 'complex'
    elif isinstance(value, str):
      return 'str'
    elif isinstance(value, datetime):
      return 'datetime'
    elif isinstance(value, date):
      return 'date'
    elif isinstance(value, list):
      return 'list'
    elif isinstance(value, set):
      return 'set'
    elif isinstance(value, dict):
      return 'dict'
    else:
      raise Exception('Write eML error: Invalid primitive data type ' + str(type(value)))
    pass

  def _getPrimitiveDataType(self, value):  # ----------------------------- _getPrimitiveDataType >>
    """
    returns the primitive data associated with the inpuy value. Valid python values are:
    bool, int, float, complex, str, date, datetime

    :param value: value to determine the data type of
    :return: the data type of the input value
    """
    # python language data types
    if isinstance(value, bool):
      return 'bool'
    elif isinstance(value, int):
      return 'int'
    elif isinstance(value, float):
      return 'float'
    elif isinstance(value, complex):
      return 'complex'
    elif isinstance(value, str):
      return 'str'
    elif isinstance(value, datetime):
      return 'datetime'
    elif isinstance(value, date):
      return 'date'
    elif isinstance(value, np.bool_):
      return 'bool'
    elif isinstance(value, np.int8):
      return 'int8'
    elif isinstance(value, np.uint8):
      return 'uint8'
    elif isinstance(value, np.int16):
      return 'int16'
    elif isinstance(value, np.uint16):
      return 'uint16'
    elif isinstance(value, np.int32):
      return 'int32'
    elif isinstance(value, np.intc):
      return 'intc'
    elif isinstance(value, np.uint32):
      return 'unit32'
    elif isinstance(value, np.uintc):
      return 'uintc'
    elif isinstance(value, np.intp):
      return 'intp'
    elif isinstance(value, np.uintp):
      return 'uintp'
    elif isinstance(value, np.int32):
      return 'int32'
    elif isinstance(value, np.int64):
      return 'int64'
    elif isinstance(value, np.uint32):
      return 'uint32'
    elif isinstance(value, np.uint64):
      return 'uint64'
    elif isinstance(value, np.float16):
      return 'float16'
    elif isinstance(value, np.float32):
      return 'float32'
    elif isinstance(value, np.float64):
      return 'float64'
    elif isinstance(value, np.float96):
      return 'float96'
    elif isinstance(value, np.float128):
      return 'float128'
    elif isinstance(value, np.complex64):
      return 'complex64'
    elif isinstance(value, np.complex128):
      return 'complex128'
    elif isinstance(value, np.complex192):
      return 'complex192'
    elif isinstance(value, np.complex256):
      return 'complex256'
    else:
      raise Exception('Write eML error: Invalid primitive data type ' + str(type(value)))
    pass

  def _isPrimitive(self, value):  # ----------------------------------------------- _isPrimitive >>
    """
    Determines if the input value is a primitie data type.

    :param value: value to determine the data type of
    :return: True if value is of type primitive, False otherwise
    """
    # python language data types
    if isinstance(value, bool):
      return True
    elif isinstance(value, int):
      return True
    elif isinstance(value, float):
      return True
    elif isinstance(value, complex):
      return True
    elif isinstance(value, str):
      return True
    elif isinstance(value, datetime):
      return True
    elif isinstance(value, date):
      return True
    elif isinstance(value, np.bool_):
      return True
    elif isinstance(value, np.int8):
      return True
    elif isinstance(value, np.uint8):
      return True
    elif isinstance(value, np.int16):
      return True
    elif isinstance(value, np.uint16):
      return True
    elif isinstance(value, np.int32):
      return True
    elif isinstance(value, np.intc):
      return True
    elif isinstance(value, np.uint32):
      return True
    elif isinstance(value, np.uintc):
      return True
    elif isinstance(value, np.intp):
      return True
    elif isinstance(value, np.uintp):
      return True
    elif isinstance(value, np.int32):
      return True
    elif isinstance(value, np.int64):
      return True
    elif isinstance(value, np.uint32):
      return True
    elif isinstance(value, np.uint64):
      return True
    elif isinstance(value, np.float16):
      return True
    elif isinstance(value, np.float32):
      return True
    elif isinstance(value, np.float64):
      return True
    # elif isinstance(value, np.float96):
    #   return True
    # elif isinstance(value, np.float128):
    #   return True
    elif isinstance(value, np.complex64):
      return True
    elif isinstance(value, np.complex128):
      return True
    # elif isinstance(value, np.complex192):
    #   return True
    # elif isinstance(value, np.complex256):
    #   return True
    else:
      return False



  def _getArrayDataType(self, value: np.ndarray):  # ------------------------- _getArrayDataType >>
    """

    :param value:
    :return:
    """
    tmp = value.flatten()
    dt = self._getPrimitiveDataType(tmp[0])
    for currval in tmp:
      if dt != self._getPrimitiveDataType(currval):
        return ''

    return str(dt)
    pass
