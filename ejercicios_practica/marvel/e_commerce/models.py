from django.db import models
from django.contrib.auth.models import User  # Para utilizar el modelo User de Django


# Modelo Comic existente
class Comic(models.Model):
    '''
    Esta clase hereda de Django models.Model y crea una tabla llamada
    e_commerce_comic. Las columnas toman el nombre especificado de cada objeto.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    marvel_id = models.PositiveIntegerField(
        verbose_name='marvel id', null=False, blank=False, unique=True
    )
    title = models.CharField(
        verbose_name='title', max_length=120, default=''
    )
    description = models.TextField(verbose_name='description', default='')
    price = models.FloatField(
        verbose_name='price', max_length=5, default=0.00
    )
    stock_qty = models.PositiveIntegerField(
        verbose_name='stock qty', default=0
    )
    picture = models.URLField(verbose_name='picture', default='')

    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades como el nombre de la tabla.
        '''
        db_table = 'e_commerce_comics'
        verbose_name = 'comic'
        verbose_name_plural = 'comics'

    def __str__(self):
        '''
        El método __str__ cumple una función parecida a __repr__ en SQL Alchemy, 
        es lo que retorna cuando llamamos al objeto.
        '''
        return f'{self.id}'


# Nueva clase WishList
class WishList(models.Model):
    '''
    Esta clase representa la lista de deseos (wish list) de un usuario, 
    con los comics que están en su lista de deseos, en el carrito o comprados.
    '''
    id = models.BigAutoField(db_column='ID', primary_key=True)
    
    # Relación con el modelo User (un usuario puede tener múltiples wishlists)
    user = models.ForeignKey(
        User,
        verbose_name='User',
        on_delete=models.CASCADE  # Al eliminar el usuario, se eliminan sus wishlists
    )
    
    # Relación con el modelo Comic (un comic puede estar en múltiples wishlists)
    comic = models.ForeignKey(
        Comic,
        verbose_name='Comic',
        on_delete=models.CASCADE,  # Al eliminar el comic, se eliminan las relaciones en wishlists
        default=1,
        blank=True
    )
    
    # Campos adicionales
    favorite = models.BooleanField(
        verbose_name='Favorite', 
        default=False  # Si es verdadero, el comic es un favorito
    )
    cart = models.BooleanField(
        verbose_name='In Cart', 
        default=False  # Si es verdadero, el comic está en el carrito de compras
    )
    wished_qty = models.PositiveIntegerField(
        verbose_name='Wished Quantity',
        default=1  # Cantidad deseada del comic
    )
    bought_qty = models.PositiveIntegerField(
        verbose_name='Bought Quantity',
        default=0  # Cantidad comprada del comic
    )

    class Meta:
        '''
        Con "class Meta" podemos definir atributos de nuestras entidades como el nombre de la tabla.
        '''
        db_table = 'e_commerce_wishlist'
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'

    def __str__(self):
        '''
        Método que retorna una representación del objeto.
        '''
        return f'{self.user.username} - {self.comic.title}'

