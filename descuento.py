print ('Una tienda ofrece el 15% de descuento en todas sus compras y el cliente quiere saber cuanto debe de pagar en total')

precio = float(input('Ingrese el costo del producto $'))

#Una vez que tenemos el precio original calculamos el 15% de descuento a este.

descuento = precio * 0.15

#Ahora calculamos el precio final que va pagar el cliente una vez descubierto el descuento.

totalapagar = precio - descuento

print ('\nTiket de la tiendita feliz\n')
print (f'Precio del producto ${precio}')
print (f'descuento ${descuento:.2f}')
print (f'Total a pagar ${totalapagar:.2f}')
print ('\nGRACIAS POR SU COMPRA\n')
