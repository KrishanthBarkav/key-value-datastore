import datastore

ds = datastore.DataStore('test.json', 'New User')

ds.Create(key="H56GDB", val="I'm Indian", time=0)               # creating a new entry with no time to live

ds.Create(key="B73FD4", val="I love football", time=10)         # creating a new entry with 10secs time to live

ds.Create(key="H56GDB", val="I listen to Guns n Roses", time=0)  # creating a new entry with duplicate key

ds.Read(key="H56GDB")                                           # reading an entry

ds.Create(key="B56FV9", val="Have a good day", time=0)

ds.Delete(key="B56FV9")



