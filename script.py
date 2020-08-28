class Art:
  
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return '{artist}. \"{title}\". {year}, {medium}. {owner}, {location}.'.format(artist = self.artist, title = self.title, year = str(self.year), medium = self.medium, owner = self.owner.name, location = self.owner.location)



class Marketplace:
  
  def __init__(self):
    self.listings = []
  
  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, i):
    self.listings.remove(i)
  
  def show_listings(self):
    for listing in self.listings:
      return self.listings


class Client:

  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum

  def sell_artwork(self, artwork, price):
    self.price = price
    self.artwork = artwork
    if self.artwork.owner.name == self.name:
      veneer.add_listing(Listing(self.artwork.title, self.price, self.artwork.owner.name))
      

  def buy_artwork(self, artwork):
    self.artwork = artwork
    if self.artwork.owner.name != self:
      for listing in veneer.listings:
        if listing.art == self.artwork.title:
          self.artwork.owner = self
          veneer.remove_listing(listing)
          return 'Congrats on your purchase! You bought the {a} for {p}'.format(a = self.artwork.title , p = listing.price)
        else:
          return "Sorry, We don\'t have that!"

          
          

class Listing(Client):

  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return '{art}: {price}.'.format(art = self.art, price = self.price)


veneer = Marketplace()

edytta = Client('Edytta Halpirt', 'Private Collection', 'No')

moma = Client('The MOMA', 'New York', 'Yes')


girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', 1910, edytta)


edytta_add_listing = edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')




moma_purchase = moma.buy_artwork(girl_with_mandolin)
#print(moma_purchase)
#print(girl_with_mandolin)
#print(veneer.show_listings())
