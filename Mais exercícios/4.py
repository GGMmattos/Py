#Se o parâmetro da função for divisível por 3 retorne Fizz, se o parâmetro da função for divisível por 5 retorne Buzz
#se  for  divisivel por 3 e 5 retorn FizzBuzz, ja se não for divisível por nenhum dos numero retorne o parâmetro.
def FizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return"FIZZBUZZ"
    if num % 3 == 0:
        return"FIZZ"
    if num % 5 == 0:
        return"BUZZ"
    return num
resu = FizzBuzz(11)
print(resu)