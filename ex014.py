## Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# (0°C × 9/5) + 32 = 32°F

celsius = int(input('Digite quantos graus está agora (em graus Celsius): '))

fahrenheit = (celsius * (9 / 5)) + 32

print(f'Graus Celsius: {celsius}°C.')
print(f'Graus Fahrenheit: {fahrenheit}°F.')

