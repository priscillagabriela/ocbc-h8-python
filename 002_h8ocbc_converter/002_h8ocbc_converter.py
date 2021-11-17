def kelvincelcius(degrees,init,tobe):
   '''
   Function kelvincelcius is used to convert temperature from kelvin to celcius or otherwise
   :param degrees: Input degrees of temperature | int
   :param init: Input initial temperature scale | string
   :param tobe: Input expected temperature scale | string
   :print: converted: Converted temperature | int
   '''
   if(tobe=='kelvin'):
       converted = degrees + 273
       unit = 'K'
   elif(tobe=='celcius'):
       converted = degrees - 273
       unit = 'C'
   print('Converted temperature from', init, 'to', tobe, 'is', converted, unit)

def tofarenheit(degrees,init):
   '''
   Function tofarenheit is used to convert temperature from kelvin or celcius to farenheit
   :param degrees: Input degrees of temperature | int
   :param init: Input initial temperature scale | string
   :print: converted: Converted temperature | int
   '''
   if(init=='kelvin'):
       converted = 9/5 * (degrees-273) + 32
   elif(init=='celcius'):
       converted = (9/5) * degrees + 32
   print('Converted temperature from', init, 'to farenheit is', converted, 'F')

def fromfarenheit(degrees,tobe):
   '''
   Function fromfarenheit is used to convert temperature from farenheit to kelvin or celcius
   :param degrees: Input degrees of temperature | int
   :param tobe: Input expected temperature scale | string
   :print: converted: Converted temperature | int
   '''
   if(tobe=='kelvin'):
       converted = 5/9 * (degrees-32) + 273
       unit = 'K'
   elif(tobe=='celcius'):
       converted = 5/9 * (degrees-32)
       unit = 'C'
   print('Converted temperature from farenheit to', tobe, 'is', converted, unit)

print('------------------------------------TEMPERATURE CONVERTER------------------------------------')
print('Choose the initial temperature scale (1/2/3):')
print('1. kelvin')
print('2. celcius')
print('3. farenheit')
init = input('Your chosen initial scale: ')

print('')

print('Choose the expected temperature scale (1/2/3):')
print('1. kelvin')
print('2. celcius')
print('3. farenheit')
tobe = input('Your chosen expected scale: ')

print('')

deg = input('Enter the degrees: ')

print('')

scale = ['kelvin','celcius','farenheit']

if(init==tobe):
    print('Initial and expected scale could not be the same.')
elif(init!=tobe):
    if(init=='1' or init=='2'):
        if(tobe=='1' or tobe=='2'):
            kelvincelcius(int(deg),scale[int(init)-1],scale[int(tobe)-1])
            print('')
            print('*nb', kelvincelcius.__doc__)
        elif(tobe=='3'):
            tofarenheit(int(deg),scale[int(init)-1])
            print('')
            print('*nb',tofarenheit.__doc__)
    elif(init=='3'):
        fromfarenheit(int(deg),scale[int(tobe)-1])
        print('')
        print('*nb',fromfarenheit.__doc__)