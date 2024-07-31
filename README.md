# eML
A strongly typed meta/mark-up language that maintains data types within object containers.

The resultant eML file contains one header line and one entry for each user entry specified. The 
header fline containes the following:
eML Header (idenfifying it as the header line), eML version number, lanuage that created the file, 
creation date, last modified date

There are setters for each of the python data type. The following is an example of writing simple 
primatives to an eML file and the resulantant file.

    eml = eML(eml_filename)
    eml.setBoolean('boolean', False)
    eml.setInt('int', 666)
    eml.setFloat('float', 666.666)
    eml.setComplex('complex', 1+1j)
    eml.setString('string', 'this is an eml test of the primitives')
    eml.setDate('date', datetime.today().date())
    eml.setDateTime('datetime', datetime.today())
    eml.saveAs()

Resultant eML file:

    eML Header | 0.01 | python | 07/28/2024 16:13:20.603820 | 07/28/2024 16:13:20.603820
    boolean := <bool>False
    int := <int>666
    float:= <float>666.666
    complex := <complex>(1+1j)
    string := <str>this is an eml test of the primitives
    date := <date>07/28/2024
    datetime := <datetime>07/28/2024 16:13:20.603820

The following is an example of writing simple containers to an eML file and the resulantant file.

    eml = eML(eml_filename)
    eml.setList('list1', [1, 2, 3])
    eml.setList('list2', [1, 1.3, 'yup'])
    eml.setSet('set1', {1, 2, 3})
    eml.setSet('set2', {1, 1.3, 'yup'})
    eml.setDict('dict1', {'1':1, '2':2, '3':3})
    eml.setDict('dict2', {1:1, '2':2, 3.0:3})
    eml.setTuple('tuple 1', (1,2,'g'))
    eml.saveAs()

Resultant eML file:

    eML Header | 0.01 | python | 07/28/2024 16:13:20.603820 | 07/28/2024 16:13:20.603820
    list1 := <list|3> <int>1
                      <int>2
                      <int>3
    list2 := <list|3> <int>1
                      <float>1.3
                      <str>yup
    set1 := <set|3> <int>1
                    <int>2
                    <int>3
    set2 := <set|3> <str>yup
                    <int>1
                    <float>1.3
    dict1 := <dict|3><str>1|<int>1
                     <str>2|<int>2
                     <str>3|<int>3
    dict2 := <dict|3><int>1|<int>1
                     <str>2|<int>2
                     <float>3.0|<int>3
    tuple 1 := <tuple|3> <int>1
                         <int>2
                         <str>g