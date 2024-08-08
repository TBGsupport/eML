"""
          eML_Read_Test of the eML system
   
           created by RD McCann on 8/5/2023
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
from eML import eML


class eML_Read_Test:
  def __init__(self):
    pass

  def testPrimitiveReads(self):
    eml = eML('C:\\Users\\mccan\\OneDrive\\Software\\Python\\Active\\eML\\Test\\primitive.eml')
    pass

  def testContainerReads(self):
    eml = eML('C:\\Users\\mccan\\OneDrive\\Software\\Python\\Active\\eML\\Test\\simplecontainer.eml')
    iii=0
    pass

  def testComplexContainerReads(self):
    eml = eML('C:\\Users\\mccan\\OneDrive\\Software\\Python\\Active\\eML\\Test\\complexcontainer.eml')
    iii=0
    pass


if __name__ == "__main__":
  print('enl test')

  # eML_Read_Test().testPrimitiveReads()

  eML_Read_Test().testContainerReads()

  eML_Read_Test().testComplexContainerReads()