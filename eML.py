"""
                eML of the eML system
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
import datetime
import os

from _Write_eML import _Write_eML
from _Read_eML import _Read_eML


class eML:  # ============================================================================ eML >>>
  """
  eML is a strongly typed mate/mark-up language. This facilitates the use of object containers
  whilw maintaining the data type of each element within the container.

  valid data types that are used include the following:
    Primitives:
      bool, byte, int, float, complex, str, datetime, date
    Containers:
      dict, list, set, tuple, and FrozenSet
  """
  def __init__(self, eml_filename: str = None):
    """

    :param eml_filename: the eml filename holding the eml contents
    """
    self.eml_filename = eml_filename

    # class variables
    # holds all of the eML identifiers and data as specified by the user
    self.eml_data = dict()

    # holds the identifier and the primary data type
    self.identifiers = dict()

    # the meta data for this instance of eML
    self.eml_meta_data = dict()
    self.eml_meta_data['version'] = 0.010
    self.eml_meta_data['lamguage'] = 'python'
    self.eml_meta_data['creation date'] = datetime.datetime.today()
    self.eml_meta_data['last update'] = datetime.datetime.today()

    # if there is an existing eML filename that should be used
    if eml_filename is not None:
      if os.path.exists(eml_filename):
        reml = _Read_eML(eml_filename)
        self.eml_meta_data, self.identifiers, self.eml_data = reml.getExistingData()
    pass

  def exists(self, name):  # ------------------------------------------------------------ exists >>
    """
    checks to see if the user specified identifier is within the current eML file.

    :param name: user supplied identifier
    :return: True if the name is within the current eML file, False otherwise
    """
    return name in self.eml_data
    pass

  def dropIdentifier(self, name):  # ------------------------------------------- dropIdentifier >>
    """
    Drops/Deletes the specified key from the eml_data

    :param name:  user supplied identifier
    """
    if self.exists(name):
      self.eml_data.drop(name, None)

  def getBoolean(self, name):  # --------------------------------------------------- getBoolean >>
    """
    Get a previously stored Boolean value within the current eML file.

    :param name:  user supplied identifier
    :return: boolean value of the identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return None

  def getInt(self, name):  # --------------------------------------------------- getInt >>
    """
    Get a previously stored Int value within the current eML file.

    :param name: user supplied identifier
    :return: Int value of the specified identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return None
    pass

  def getDict(self, name):  # --------------------------------------------------- getDict >>
    """
    Get a previously stored Dict value within the current eML file.

    :param name: user supplied identifier
    :return: Dict of the specified identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return dict()

  def getFloat(self, name):  # --------------------------------------------------- getFloat >>
    """
    Get a previously stored Float value within the current eML file.

    :param name: user supplied identifier
    :return: Float value of the specified identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return None

  def getComplex(self, name):  # --------------------------------------------------- getComplex >>
    """
    Get a previously stored Complex value within the current eML file.

    :param name: user supplied identifier
    :return: Complex value of the specified identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return None

  def getDate(self, name):  # --------------------------------------------------- getDate >>
    """
    Get a previously stored Date value within the current eML file.

    :param name: user supplied identifier
    :return: Date value of the specified identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return None

  def getDatetime(self, name):  # --------------------------------------------------- getDatetime >>
    """
    Get a previously stored Datetime value within the current eML file.

    :param name: user supplied identifier
    :return: Datetime value of the specified identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return None

  def getList(self, name):  # --------------------------------------------------- getList >>
    """
    Get a previously stored List value within the current eML file.

    :param name:  user supplied identifier
    :return: List of the specified identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return list()

  def getSet(self, name):  # --------------------------------------------------- getSet >>
    """
    Get a previously stored Set value within the current eML file.

    :param name:  user supplied identifier
    :return: Set of the specified identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return set()

  def getString(self, name):  # --------------------------------------------------- getString >>
    """
    Get a previously stored String value within the current eML file.

    :param name: user supplied identifier
    :return: String value of the specified identifier
    """
    if self.exists(name):
      return self.eml_data[name]
    else:
      return None

  def setBoolean(self, identifier, value: bool):  # -------------------------------- setBoolean >>
    """
    writes a boolean value to the eml file

    :param identifier: identifier for this boolean value
    :param value:  value to be written to the eml file
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'bool'

    self.eml_data[identifier] = value
    pass

  def setComplex(self, identifier, value: complex):  # ----------------------------- setComplex >>
    """
    writes a complex value to the eml file

    :param identifier: identifier for this complex value
    :param value:  value to be written to the eml file
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'complex'

    self.eml_data[identifier] = value
    pass

  def setDate(self, identifier, value: datetime.date):  # ------------------------------ setDate >>
    """
    writes a date value to the eml file

    :param identifier: identifier for this date value
    :param value:  value to be written to the eml file
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'date'

    self.eml_data[identifier] = value
    pass

  def setDateTime(self, identifier, value: datetime):  # -------------------------- setDateTime >>
    """
    writes a date time value to the eml file

    :param identifier: identifier for this date time value
    :param value:  value to be written to the eml file
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'bool'

    self.eml_data[identifier] = value
    pass

  def setDict(self, identifier, dictin: dict):  # -------------------------------------- setDict >>
    """
    Sets a dict to be output to an eML file.

    :param identifier: user specified string naming the dict for subsequent retrieval
    :param dictin: Input dict to be written to the eML file
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'dict'

    self.eml_data[identifier] = dictin
    pass

  def setFloat(self, identifier, value: float):  # ----------------------------------- setFloat >>
    """
    writes a float value to the eml file

    :param identifier: identifier for this float value
    :param value:  value to be written to the eml file
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'float'

    self.eml_data[identifier] = value
    pass

  def setFrozenSet(self, identifier, value: frozenset):  # ----------------------- setFrozenSet >>
    """
    writes a frozenset value to the eml file

    :param identifier: identifier for this frozenset value
    :param value:  value to be written to the eml file
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'frozen set'

    self.eml_data[identifier] = value
    pass

  def setInt(self, identifier, value: int):  # ------------------------------------------ setInt >>
    """
    writes a int value to the eml file

    :param identifier: identifier for this int value
    :param value:  value to be written to the eml file
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'int'

    self.eml_data[identifier] = value
    pass

  def setList(self, identifier, value: list):  # --------------------------------------- setList >>
    """
    Converts a list to string for output to linesout.

    :param identifier: user defined identifier for this set
    :param value: the list to be output to a string
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'list'

    self.eml_data[identifier] = value
    pass

  def setSet(self, identifier, value: set):  # ------------------------------------------ setSet >>
    """
    Converts a set to string for output to linesout.

    :param identifier: user defined identifier for this set
    :param value: the set to be output to a string
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'set'

    self.eml_data[identifier] = value
    pass

  def setString(self, identifier, value: str):  # ------------------------------------ setString >>
    """
    writes a string value to the eml file

    :param identifier: identifier for this string value
    :param value:  value to be written to the eml file
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'string'

    self.eml_data[identifier] = value
    pass

  def setTuple(self, identifier, value: tuple):  # ------------------------------------ setTuple >>
    """
    Converts a tuple to string for output to linesout.

    :param identifier: user defined identifier for this tuple
    :param value: the tuple to be output to a string
    """
    if identifier in self.identifiers:
      raise Exception('eML error: Identifier ' + identifier + ' already exists')
    self.identifiers[identifier] = 'tuple'

    self.eml_data[identifier] = value
    pass

  def save(self, eml_filename: str = None):  # -------------------------------------------- save >>
    """
    Writes the generated eml string to the file specified and closes the file
    """
    if eml_filename is None:
      if self.eml_filename is None:
        raise Exception('eML save error: no eml filename specified for write')
      else:
        eml_filename = self.eml_filename

    ew = _Write_eML(eml_filename, self.eml_meta_data, self.identifiers, self.eml_data)
    ew.save()
    pass

  def saveAs(self, eml_filename: str = None):  # ---------------------------------------- saveAs >>
    """
    Writes the generated eml string to the file specified and closes the file

    """
    if eml_filename is None:
      if self.eml_filename is None:
        raise Exception('eML save error: no eml filename specified for write')
      else:
        eml_filename = self.eml_filename

    ew = _Write_eML(eml_filename, self.eml_meta_data, self.identifiers, self.eml_data)
    ew.save()
    pass