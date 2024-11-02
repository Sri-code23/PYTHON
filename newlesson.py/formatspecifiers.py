#format specifiers ={value:flags}
num=6345.785
f=25.667868765
l=9
print(f"num:{num:.2f}") #prints two values after the decimal 
print(f"faa:{f:.3f}") #prints three values after the decimal 
print(f"loo:{l:.1f}") #prints one values after the decimal 
print(f"num:{num:10}")
print(f"nume:{l:10}")
print(f"nume:{f:10}")

print(f"nume:{num:<10}")
print(f"numd:{l:<10}")
print(f"numd:{f:<10}")

print(f"numesg:{num:>10}")
print(f"numdgs:{l:>10}")
print(f"numds:{f:>10}")

print(f"numdfhsdf:{num:^10}")