class Marketplace:
    def __init__(self, listings:list):
        self.listings = listings

    def add_listing(self,new_listing):
        self.listings.append(new_listing)

    def remove_listing(self,ended_listing_index):
        self.listings.pop(ended_listing_index)

    def show_listings(self):
        if len(self.listings) > 0:
            for listing in self.listings:
                print(listing)
        else:
            print("We currently have no art for sale.")


class Client:
    def __init__(self,name,location,is_museum:bool):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    def __repr__(self):
        return f"{self.name}: {self.location}"

    def sell_artwork(self,artwork,price,marketplace):
        if artwork.owner.name.upper() == self.name.upper():
            new_listing = Listing(artwork,price,self.name)
            marketplace.add_listing(new_listing)

    def buy_artwork(self,artwork,marketplace):
        if artwork.owner.name.upper() != self.name.upper():
            artwork_index = -1
            for index in range(len(marketplace.listings)):
                if artwork.title == marketplace.listings[index].art.title:
                    artwork_index = index
                    break
            if artwork_index == -1:
                print("Unable to find that piece in the marketplace.")
            if artwork_index >= 0:
                artwork.owner = self
                marketplace.remove_listing(artwork_index)


class Art:
    def __init__(self, artist, title, medium, year, owner:Client):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        return f"{self.artist}. \"{self.title}\". {self.year}, {self.medium}. Owned By: {self.owner.name}, {self.owner.location}"


class Listing:
    def __init__(self,art,price,seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return f"{self.art.title}: {self.price}"




veneer = Marketplace([])

edytta = Client("Edytta Halprit","Private Collection",False)

moma = Client("The MOMA","New York",True)

girl_with_mandolin = Art("Picasso, Pablo","Girl with a Mandolin (Fanny Tellier)","oil on canvas",1910,edytta)

print(girl_with_mandolin)
# print(edytta)
# print(moma)

edytta.sell_artwork(girl_with_mandolin,6000000,veneer)

veneer.show_listings()

moma.buy_artwork(girl_with_mandolin,veneer)

print(girl_with_mandolin)

veneer.show_listings()