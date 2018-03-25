# RandomPeople4Neo

This is a script for the demo part of my [talk on Graph Databases](http://linuxday.gulch.it/slides/2015/traccia-tecnica/dbms.pdf) I made at ["Linux Day" 2015.](http://linuxday.gulch.it/node/68) (slides are in italian).

This little script creates, in a pseudo-random way, people and relationships among them. It outputs two CSV files ready to be imported on Neo4j, in order to have a didactic database with which to play.

Tested on the current Neo4j version (3.3.4)

**The source code includes two variables that defines how much people and how much relationships generate.**


## How to

Create the datasets:

```bash
$ python randompeople4neo.py
```

Create the db (Neo4j must not be in running).

```bash
# $BASH_HOME/bin/neo4j-admin import --database people.db --nodes users.csv --relationships rels.csv
# $BASH_HOME/bin/neo4j start
```
**Note** : $BASH_HOME is wherever you have installed Neo4j.

---

If all gone well, you can now play with the db. The file `query.md` contains a few example queries. Have fun! 😃
