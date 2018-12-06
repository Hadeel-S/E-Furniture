#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///efurniture.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Sara", email="xx4@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/'
             '18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# categories
category1 = Category(name="Living Room Furniture")
session.add(category1)
session.commit()

item1_1 = Item(name="Fabric Sofa", description="Crafted by our master "
                    "upholsterers in North Carolina, our Cameron "
                    "Collection offers superb quality at an unparalleled"
                    " price. Our sofas and love seat are built with"
                    " eco-friendly materials and plush seat cushions"
                    " for maximum comfort.",
                    price="2299", color="Cream", image="https://www."
                    "potterybarn.com/pbimgs/ab/images/dp/wcm/201839/"
                    "0015/cameron-roll-arm-upholstered-sofa-"
                    "collection-1-c.jpg", category=category1, userid=1)
session.add(item1_1)
session.commit()

item2_1 = Item(name="Leather Sofa", description="Generously proportioned"
                    " and offering the best in comfort and style, our"
                    " Pearce Collection was designed to accommodate every"
                    " lifestyle. Distinctive, generous arms "
                    "and luxuriously deep seat cushions make our Square"
                    " Arm Leather Sofas one of our most welcoming and "
                    "substantial seating options.",
                    price="3599", color="Espresso", image="https://www."
                    "potterybarn.com/pbimgs/ab/images/dp/wcm/201839/"
                    "0015/chesterfield-leather-sofa-c.jpg",
                    category=category1, userid=1)
session.add(item2_1)
session.commit()

category2 = Category(name="Dining & Kitchen Furniture")
session.add(category2)
session.commit()

item1_2 = Item(name="Extending Dining Table", description="Inspired by "
                    "the spirited, industrial character of an early "
                    "20th century work table, the Benchwright Extending"
                    " Dining Table provides a bold backdrop for creative"
                    " entertaining. Grooves and saw marks on the wood "
                    "surface create the look of salvaged lumber, and "
                    "oversized bolts on the legs and tabletop add to "
                    "its rustic feel. Two drop in leaves allow "
                    "seating for a large gathering.",
                    price="2499", color="Seadrift", image="https://www."
                    "potterybarn.com/pbimgs/ab/images/dp/wcm/201838/"
                    "0066/benchwright-extending-dining-table-c.jpg",
                    category=category2, userid=1)
session.add(item1_2)
session.commit()

category3 = Category(name="Bedroom Furniture")
session.add(category3)
session.commit()

item1_3 = Item(name="Farmhouse Bed", description="Style, simplicity and"
                    " fine craftsmanship are the hallmarks of classic"
                    " Shaker furniture. With our Farmhouse collection,"
                    " we not only honor but also build on these qualities.",
                    price="1599", color="Gray Wash", image="https://www."
                    "potterybarn.com/pbimgs/ab/images/dp/wcm/201849/0389/"
                    "farmhouse-bed-c.jpg", category=category3, userid=1)
session.add(item1_3)
session.commit()

item2_3 = Item(name="Farmhouse Dresser", description="Beautiful "
                    "craftsmanship and fine hardwood construction"
                    " give our Farmhouse Dresser lasting style. Providing"
                    " ample storage, it features four fully finished dovetail"
                    " drawers with decorative keyhole hardware.",
                    price="1299", color="Gray Wash", image="https://www."
                    "potterybarn.com/pbimgs/ab/images/dp/wcm/201849/0386/"
                    "farmhouse-dresser-d.jpg", category=category3, userid=1)
session.add(item2_3)
session.commit()

category4 = Category(name="Home Office Furniture")
session.add(category4)
session.commit()

item1_4 = Item(name="Livingston Small Desk", description="The wood rich grain"
                    " enhanced with a gray or brown wash gives our Livingston "
                    "collection a naturally weathered look that accentuates "
                    "its fine classic details. The Small Desk "
                    "rests on a plinth base"
                    " and is detailed with molding and"
                    " fluting on the posts. Pair it with other"
                    " modular components in the collection to"
                    " create an office or work space that is both stylish and "
                    "filled with functionality.",
                    price="1234", color="Gray Wash", image="https://www."
                    "potterybarn.com/pbimgs/ab/images/dp/wcm/201849/0205/"
                    "livingston-small-desk-c.jpg",
                    category=category4, userid=1)
session.add(item1_4)
session.commit()

item2_4 = Item(name="Livingston Wall Suite With Drawers", description="The"
                    " wood rich grain enhanced with a brown wash gives the "
                    "Livingston Collection a naturally weathered look that "
                    "accentuates its fine classic details like plinth bases,"
                    " crown molding and fluting on the posts. Pair the Wall "
                    "Suite with Drawers with other pieces in the collection "
                    "to customize an office, media or work space that is both"
                    " stylish and filled with functionality.",
                    price="2361", color="Gray Wash", image="https://www."
                    "potterybarn.com/pbimgs/ab/images/dp/wcm/201847/0013/"
                    "livingston-wall-suite-with-drawers-i.jpg",
                    category=category4, userid=1)
session.add(item2_4)
session.commit()

category5 = Category(name="Outdoor Furniture")
session.add(category5)
session.commit()

item1_5 = Item(name="Sheldon Flatweave Rug", description="With a minimal"
                    " pattern inspired by Moroccan tiles, the Sheldon "
                    "Flatweave Rug brings a sophisticated look to floors.",
                    price="489", color="Blue", image="https://www."
                    "potterybarn.com/pbimgs/ab/images/dp/wcm/201846/"
                    "0042/sheldon-flatweave-rug-blue-ivory-i.jpg",
                    category=category5, userid=1)
session.add(item1_5)
session.commit()

item2_5 = Item(name="Round Market Umbrella - Stripe", description="Vibrant,"
                    " sun-drenched colors make these umbrellas summer "
                    "favorites. A choice of fabrics and poles helps you"
                    " complement outdoor furnishings.",
                    price="749", color="Black", image="https://www."
                    "potterybarn.com/pbimgs/ab/images/dp/wcm/201832/0009/"
                    "round-market-umbrella-stripe-i.jpg",
                    category=category5, userid=1)
session.add(item2_5)
session.commit()
print("added categories!")
