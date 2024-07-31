"""
            eStringUtils of the eML system
                eOr's Meta Language

           created by RD McCann on 7/27/2023
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

def subString(from_string:str, start_delimiter, end_delimiter):
  if start_delimiter in from_string:
    interim_string = from_string.strip(start_delimiter)[1]

    if end_delimiter in interim_string:
      stringout = interim_string.strip(end_delimiter)[0]
      return stringout

  return ''
  pass


def beforeFirst(strin, parse_character):  # ---------------------------------------- beforeFirst >>
  """

  :param strin:
  :param parse_character:
  :return:
  """
  indx = strin.find(parse_character)
  return strin[:indx]
  pass


def afterFirst(strin, parse_character):  # ---------------------------------------- beforeFirst >>
  """

  :param strin:
  :param parse_character:
  :return:
  """
  indx = strin.find(parse_character)
  return strin[indx+1:]
  pass