

notas=(12,56,57,89,90,97,45,63,82,16)
a = int(input("inserte rimer nota:"))
                
mayor=0
menir=100
for i in notas:
    if i> mayor:
        mayor=i
    if i<menir:
        menir=i

aprob=0
desapro=0
for i in notas:
    if i >=70:
        aprob=aprob+1
        
    else:
        desapro=desapro+1
        
print("nota mayor", mayor)
print("nota menor", menir)

print("aprobados:",aprob)
print("reprobados:",desapro)
