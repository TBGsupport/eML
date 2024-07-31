"""
            eML_Write_Test of the eML system
           created by RD McCann on 7/31/2023
    Copyright (c) 2023 Turtle Bay Geophysical LLC
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

from eML import eML


class eML_Write_Test:

  def testPrimitiveWrites(self):
    eml = eML('C:\\Users\\mccan\\OneDrive\\Software\\Python\\Active\\eML\\Test\\primitive.eml')
    eml.setBoolean('boolean', False)
    # eml.setByte('Byte', bytes('byte test', 'utf-8'))
    eml.setInt('int', 666)
    eml.setFloat('float', 666.666)
    eml.setComplex('complex', 1+1j)
    eml.setString('string', 'this is an eml test of the primitives')
    eml.setDate('date', datetime.today().date())
    eml.setDateTime('datetime', datetime.today())
    eml.saveAs()
    pass

  def testContainerWrites(self):
    eml = eML('C:\\Users\\mccan\\OneDrive\\Software\\Python\\Active\\eML\\Test\\simplecontainer.eml')
    eml.setList('list1', [1, 2, 3])
    eml.setList('list2', [1, 1.3, 'yup'])
    eml.setSet('set1', {1, 2, 3})
    eml.setSet('set2', {1, 1.3, 'yup'})
    eml.setDict('dict1', {'1':1, '2':2, '3':3})
    eml.setDict('dict2', {1:1, '2':2, 3.0:3})
    eml.setTuple('tuple 1', (1,2,'g'))
    eml.saveAs()
    pass

  def testComplexContainerWrites(self):
    list1 = [1,2,34,4]
    list2 = [2,'q',7,datetime.today()]
    set1 = {3,4,3,6}
    set2 = {4,'qs',7,datetime.today()}
    dict1 = {'a':5,'b':2, 'c':3}
    dict2 = {'a':6,2:2, 'c':3}
    dict3 = {'a':7,'b':2, 'c':datetime.today().date()}
    dict4 = {'a':8,2:2, 'c':datetime.today()}
    dict5 = {'a':9,2:2, 'c': {'c':0, 'ff':[1,2, 3,4], 'f':{'d':'d', 'f':'f', 'g':3}}}

    eml = eML('C:\\Users\\mccan\\OneDrive\\Software\\Python\\Active\\eML\\Test\\complexcontainer.eml')
    eml.setList('complex list 1', [list1, list2, set1, set2, dict1, dict2, dict3, dict4])
    eml.setDict('complex dict 1', {'a':dict1, 2:dict2, datetime.today():dict3, 4:dict4,
                                   5:dict5})
    eml.saveAs()
    pass


if __name__ == "__main__":
  print('eML test')

  eML_Write_Test().testPrimitiveWrites()
  #
  eML_Write_Test().testContainerWrites()
  #
  eML_Write_Test().testComplexContainerWrites()