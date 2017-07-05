# LandXML

Overview:

Create an XML document(s) from specified google docs for use in the Land app. Google docs must follow the format specified below. 
Some cleanup tools are implemented to correct common formatting errors. 

*****

Dependencies:

Python 3.0 or later plus standard library

Pydrive (pip install pydrive)

Presence of client_secrets.json and xmlDocs/ in execution folder. 

*****

Command Line + Arguments:

Python CreateXML countryFile 

When a single argument is present the script interprets that argument as the name of a file with the following format
Each line of that file specifies the root name of a country and the drive folder ID where the content lives. For example, the line "england,0B30rCerFhcqTVlN0Z1FEWTlRQlE" would specify the creation of an XML document with root node "england" with the content from https://drive.google.com/drive/folders/0B30rCerFhcqTVlN0Z1FEWTlRQlE
Each entry should be on it's own line with no spaces. For an example, see countries.csv

or

Python CreateXML countryName folderID 

Creates an XML document with root name countryName and content from the drive folder with ID folderID

*****

High-level description:

The file CreateXML.py is the only file that needs to be executed. First, a connection to google drive is made through the PyDrive library.
This connection is dependent on the client_secrets.json file being present in the CD and the current browser user having access to the
folders specified in the arguments. For each specified country/folderID pair, all of the files in the specified folder will be downloaded and their contents will be stored as the value in dictionary with the file number as the key. That file number will be specified at the beginning of the filename in drive. Once the files are downloaded, their contents will be iterated on by key and will be added to the XML document in the LAND format. Before the complete XML doc is output, the string is "prettified" to make the content more human-readable.

*****

Google Doc Formatting:

The file name must be the file number which is where in the order that file should go followed by a space "-" space and then a file name for reference.
The contents of the file should in the following order with each element separated by two blank lines: Navigation title, Navigation icon,
Item title, Item description, Item title, Item description... Keep in mind that any bolds/underlines will be lost in the XML creation.

Example document

File name: 6 - Trust Us, It's SIM(ple): Find The Right Plan For you

Trust Us, It's SIM(ple): Find The Right Plan For you


phoneicon.png


*Disclaimer: the following information can only be applied to an unlocked phone. If you don’t have one we highly recommend calling your phone company to unlock it before your trip :)*

You couldn’t be in a better country for cheap, convenient, accessible, no-strings-attached sim card deals. In all my years of living abroad and wrestling with foreign phone companies, I can categorically say that Britain is the king for this stuff. Here’s a breakdown: 


Best Sim for the City Hopper and Dweller: GiffGaff


For those who don’t need rural reception and want to take advantage of the best phone deal, then look no further than Giffgaff. Giffgaff offer fantastic 30 day rolling sim only deals and the best rates for 4G data and minutes in the UK. They don’t believe in long-term phone contracts so offer flexible, no-strings, ‘cancel when you want’ sims. Here’s how the prices break down: 

£5 Goodybag  -  100 mb data, 150 minutes and 500 texts
£7.50 Goodybag -  750 mb data, 250 minutes and unlimited texts
£10 Goodybag - 2 GB data, 500 minutes and unlimited texts
£12 Goodybag - 3 GB data, 750 minutes and unlimited texts
£15 Goodybag - 5 GB data, 1000 minutes and unlimited texts
£18 Goodybag - 6 GB data, 2000 minutes and unlimited texts
£20 Goodybag - Unlimited data, unlimited minutes and unlimited texts. 


How To Top Up on GiffGaff


Go to the Giffgaff website and select your favoured plan. A free sim will be posted to you (takes 3-5 days in Britain, 5 days in Europe). You’ll need to create an account and register your new sim once it arrives - a process with which you’ll be guided through. Then all you need to do is top up online and then purchase the Goodybag. If you go over your allowance you’ll be charged at the standard pay-as-you-go rates so watch out. 
When you want to cancel, simply log in to your online account and cancel. You’ll then be refunded any remaining credit on your account. Pretty simple really. 


Best Sim Company for the UK Rural Traveler: EE


EE are comprised of both Orange and T-mobile networks and have the best coverage in the UK with very little black spots. They offer a ‘pay as you go’ sim card but with the opportunity to buy ‘packs’ of data and minutes with your credit. The sim card is free with the packs lasting 30 days at a time. Considering the extensive coverage, they’re really good value for money and my chosen provider. Once you top up you will be offered the opportunity to purchase either a: 

£5 Everything Pack - 150 mb data, 250 texts and 50 minutes 
£10 Data Pack - 1 gb data, 1000 texts and 100 minutes
£10 Everything Pack - 500 mb data, unlimited texts and 150 minutes
£15 Data Pack - 4 gb data, unlimited texts and 250 minutes 
£15 Everything Pack - 2 gb data, unlimited texts and 500 minutes
£25 Everything Pack - 5 gb data, unlimited texts and 1000 minutes 

If you’re needing a sim card for a week or extended stay in the UK then this is your company. Although some companies will offer slightly cheaper deals on pay as you go ‘all data packs’, EE has the best 3G and 4G coverage in the UK.


How to Top Up on EE


Topping up can either be done online, in store, or through your phone. You’ll find EE stores on every main street in the cities here (two on Princes Street if you’re in Edinburgh, three in Glasgow with one on Buchanan Street). The online process is very simple - once you’ve purchased a sim, you’ll be prompted to create an online account through their website. Here you’ll find instructions to top up. If you need to do it through your phone, EE provide you with internet to access their website to then top up remotely. 

 
Best Sim Cards for European travel with a UK Provider: 3 Mobile


3’s ‘pay as you go’ rates are good, but their European rates are even better. Go with the ‘Feel At Home Plan’ and you’ll be able to travel 40+ countries at the same UK ‘Pay As You Go’ rate when calling/texting back to the UK. Europe, China, America and Australia included. They’ve figured out that they save UK customers an average of $270 in roaming charges through their low cost ‘add-on’ packs. It’s also free to receive calls and texts in all their ‘Feel At Home’ locations. Here is a strong disclaimer however  - the packs only provide the UK rates when calling/texting back to the UK, not to international numbers or the ones local to you outwith of the UK.  However, the data allowances as part of the ‘feel at home’ pack obviously remain the same as you travel between countries which make it such a good deal considering many of us call/text using online apps such as Whatsapp and Skype. 
The process of purchasing and topping up is similar to that of EE’s - you buy a sim card either in-store or online, create your account (My3), top up using one of the three methods (in store, online, by phone (call 444 from your sim), and then purchase the add-ons that are available to you through your new ‘my3’ account (If you don’t have a smartphone, you can continue to buy an add on by phone using the 444 number). 
Three has vastly improved as a company with a huge boost to their network coverage recently. I have had good experiences with their international coverage and have heard good reviews with more remote locations too. 
