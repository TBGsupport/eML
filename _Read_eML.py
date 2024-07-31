"""
              _Read_eML of the eML system
           created by RD McCann on 7/27/2024
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
from datetime import datetime

import eStringUtils


class _Read_eML:
  """
  Reads and parses an eML file.
  valid data types that are used include the following:
    Primitives:
      bool, byte, int, float, complex, str, datetime, date
    Containers:
      dict, list, set, tuple, and FrozenSet
  """

  def __init__(self, eML_filename):  # ------------------------------------------------ __init__ >>
    """
    Loads all information within the eML_filename. The routine reads all lines and then decomposing
    them. The individual elements can be downloaded using the get methods for each type.

    :param eML_filename: name of the eml file
    """
    self.eml_meta_data = dict()

    self.eml_data = dict()

    self.identifiers = dict()

    hasHeader = False

    with open(eML_filename) as file:
      self.linesin = [line.rstrip() for line in file]

    while len(self.linesin) > 0:
      # reads through all of the lines of the eML_filename
      line = self.linesin.pop(0)

      if 'eML Header' in line:
        hasHeader = True

        header = line.split('|')
        self.eml_meta_data['version'] = float(header[1].strip())
        self.eml_meta_data['lamguage']  = header[2].strip()
        self.eml_meta_data['creation date']  = datetime.strptime(header[3].strip(),
                                                                 '%m/%d/%Y %H:%M:%S.%f')
        self.eml_meta_data['last update']  = datetime.strptime(header[4].strip(),
                                                               '%m/%d/%Y %H:%M:%S.%f')

      elif ':=' in line:
        # all base lines have a := within the line
        tmp = line.split(':=')
        name = tmp[0].strip()
        format_n_value = tmp[1].strip()

        format, value = self._getFormatValue(format_n_value)

        self.eml_data[name] = self._decomposeEntry(format, value)
    pass

  def getExistingData(self):  # --------------------------------------------- getExistingData >>
    """
    passes all of the decomposed data for this eML file to the calling rooutine.
    :return: 3 dicts containing eml_meta_data, identifiers, eml_data
    """
    return self.eml_meta_data, self.identifiers, self.eml_data
    pass

  def _decomposeDict(self, number_of_elements: int, dictin: str):  # ----------- _decomposeDict >>
    """
    Decomposes a Dict

    :param number_of_elements: the number of elements in the Dict (string)
    :param dictin: the Dict (string)
    :return: the decomposed Set
    """
    dictout = dict()

    # decompose initial value
    keyvalue, valueformat, value = self._decomposeKeyValue(dictin)

    dictout[keyvalue] = self._decomposeEntry(valueformat, value)

    for ii in range(number_of_elements - 1):
      currline = self.linesin.pop(0)

      keyvalue, valueformat, value = self._decomposeKeyValue(currline)

      dictout[keyvalue] = self._decomposeEntry(valueformat, value)

    return dictout
    pass

  def _decomposeEntry(self, format, value):  # --------------------------------- _decomposeEntry >>
    """
    primary entry into the various decompose routines. This parses the entry into it's respectful
    decompose routine.

    :param format: the format of the entry (string)
    :param value: the string value of the entry
    :return: the decomposed data for the string entry
    """
    if self._isPrimitive(format[0]):
      # base level Primitive declaration
      return self._decomposePrimitive(format[0], value)
    else:
      # base level collection/container declaration
      match (format[0].strip()):
        case 'dict':
          return self._decomposeDict(int(format[1]), value)
        case 'list':
          return self._decomposeList(int(format[1]), value)
        case 'set':
          return self._decomposeSet(int(format[1]), value)
        case 'tuple':
          return self._decomposeTuple(int(format[1]), value)
        case _:
          raise Exception(
            'Read_eML format error: format ' + str(format) + ' is not supported')
    pass

  def _decomposePrimitive(self, format, value):  # ------------------------- _decomposePrimitive >>
    """
    Decomposes a single primitive value

    :param format: the format type of the primitive (string)
    :param value: the value of the primitive (string)
    :return: the decomposed value
    """
    match (format):
      case 'bool':
        return bool(value)
      case 'byte':
        return bytes(list[value])
      case 'int':
        return int(value)
      case 'float':
        return float(value)
      case 'complex':
        return complex(value)
      case 'str':
        return value
      case 'datetime':
        return datetime.strptime(value, '%m/%d/%Y %H:%M:%S.%f')
      case 'date':
        return datetime.strptime(value, '%m/%d/%Y').date()
      case _:
        raise Exception('Read_eML error: invalid primitive type ' + str(format))
    pass

  def _decomposeList(self, number_of_elements: int, valuein):  # --------------- _decomposeList >>
    """
    Decomposes a list

    :param number_of_elements: the number of elements in the list
    :param valuein: the list (string)
    :return: the decomposed list
    """
    listout = list()

    # decompose initial value
    format, value = self._getFormatValue(valuein)

    listout.append(self._decomposeEntry(format, value))

    for ii in range(int(number_of_elements) - 1):
      currline = self.linesin.pop(0).strip()

      format, value = self._getFormatValue(currline)

      listout.append(self._decomposeEntry(format, value))

    return listout
    pass

  def _decomposeSet(self, number_of_elements: int, valuein: str):  # ------------- _decomposeSet >>
    """
    Decomposes a Set

    :param number_of_elements: the number of elements in the Set (string)
    :param valuein: the value of the Set (string)
    :return: the decomposed Set
    """
    setout = set()

    # decompose initial value
    format, value = self._getFormatValue(valuein)

    setout.add(self._decomposeEntry(format, value))

    for ii in range(number_of_elements - 1):
      currline = self.linesin.pop(0).strip()

      format, value = self._getFormatValue(currline)

      setout.add(self._decomposeEntry(format, value))

    return setout
    pass

  def _decomposeFrozenSet(self, number_of_elements: int, valuein: str):  #-- _decomposeFrozenSet >>
    """
    Decomposes a Frozenset

    :param number_of_elements: the number of elements in the Frozenset (string)
    :param valuein: the value of the Frozenset (string)
    :return: the decomposed Frozenset
    """
    setout = set()

    # decompose initial value
    format, value = self._getFormatValue(valuein)

    setout.add(self._decomposeEntry(format, value))

    for ii in range(number_of_elements - 1):
      currline = self.linesin.pop(0).strip()

      format, value = self._getFormatValue(currline)

      setout.add(self._decomposeEntry(format, value))

    return frozenset(setout)
    pass

  def _decomposeTuple(self, number_of_elements: int, valuein: str):  # --------- _decomposeTuple >>
    """
    Decomposes a Tuple

    :param number_of_elements: the number of elements in the Tuple (string)
    :param valuein: the Tuple (string)
    :return: the decomposed Set
    """
    listout = list()

    # decompose initial value
    format, value = self._getFormatValue(valuein)

    listout.append(self._decomposeEntry(format, value))

    for ii in range(number_of_elements - 1):
      currline = self.linesin.pop(0).strip()

      format, value = self._getFormatValue(currline)

      listout.append(self._decomposeEntry(format, value))

    return tuple(listout)
    pass

  def _decomposeKeyValue(self, dictin: str):  # ---------------------------- _decomposeKeyValue >>
    """

    :param dictin:
    :return:
    """
    # tmp = arrayin.split('|')
    key = eStringUtils.beforeFirst(dictin, '|').strip()
    value = eStringUtils.afterFirst(dictin, '|').strip()
    # value = tmp[1:]
    keyformat, keyvalue = self._getFormatValue(key)
    keyvalue = self._decomposePrimitive(keyformat[0], keyvalue)
    valueformat, value = self._getFormatValue(value)
    return keyvalue, valueformat, value
    pass

  def _isPrimitive(self, format):  # ---------------------------------------------- _isPrimitive >>
    """
    determines if the input format is a rpimitive

    :param format: format of the data in question
    :return: True if it is a primitive type, False otherwise
    """
    match format:
      case 'bool' | 'int' | 'float' | 'complex' | 'str' | 'datetime' | 'date':
        return True
      case _:
        return False
    pass

  def _getFormatValue(self, format_n_value: str):  # -------------------------- _getFormatValue >>
    """

    :param format_n_value:
    :return:
    """
    indx1 = format_n_value.find('<')
    indx2 = format_n_value.find('>')
    format = format_n_value[indx1 + 1:indx2].split('|')

    value = format_n_value[indx2 + 1:]

    return format, value
    pass
