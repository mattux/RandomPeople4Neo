// -------* warm-up
MATCH (n:Person)-[r:FRIEND_OF|COLLEAGUE_OF]-(m:Person)
RETURN count(r)


// -------* how many friends have each user
MATCH (n:Person)-[r:FRIEND_OF]->()
WITH id(n) AS ID, n.name AS Name, n.surname AS Surname, r
RETURN ID, Name, Surname, count(r) as RelationshipsCount
ORDER BY RelationshipsCount DESC


// -------* every "Alice"
MATCH (n:Person)
WHERE n.name='Alice'
RETURN n


// -------* every "Alice" that are software developers (using labels)
MATCH (n:`Software Developer`)
WHERE n.name='Alice'
RETURN n


// -------* every "Alice" that are software developers (using properties)
MATCH (n:Person)
WHERE n.name='Alice' AND n.job='Software Developer'
RETURN n


// -------* friends of the first "Alice" found in our database
MATCH (n:Person)
WHERE n.name = "Alice"
WITH n LIMIT 1
MATCH (n)-[r:FRIEND_OF]->(m:Person)
RETURN n,r,m


// -------* friends of friends of the first "Alice" found in our database
MATCH (n:Person)
WHERE n.name = "Alice"
WITH n LIMIT 1
MATCH (n)-[r:FRIEND_OF*1..2]->(m:Person)
RETURN n,r,m

// or... (better way)
MATCH (n:Person)
WHERE n.name = "Alice"
WITH n LIMIT 1
MATCH p=(n)-[:FRIEND_OF*1..2]->(m:Person)
WITH *, relationships(p) AS r
RETURN n,r,m


// -------* friends of the "Alice"s
MATCH (n:Person)-[r:FRIEND_OF]->(m:Person)
WHERE n.name = "Alice"
RETURN n,r,m


// -------* relationships among all the "Alice"
MATCH (n:Person)-[r:FRIEND_OF|COLLEAGUE_OF]-(m:Person)
WHERE n.name='Alice' AND m.name="Alice"
RETURN n,m,r


// -------* friendships in common among all the "Alice" (that are friends or colleagues)
MATCH (n:Person)-[:FRIEND_OF|COLLEAGUE_OF]-(m:Person)
WHERE n.name='Alice' AND m.name="Alice"
WITH n,m
MATCH (n)-[r1:FRIEND_OF]-(p:Person)-[r2:FRIEND_OF]-(m)
RETURN n,m,p,r1,r2


// -------* Alice friends that are colleagues of Bob
MATCH (n:`Person`)-[r1:FRIEND_OF]->(m:Person)-[r2:COLLEAGUE_OF]-(p:`Person`)
WHERE n.name='Alice' AND p.name='Bob'
RETURN n,m,p,r1,r2


// -------* all the Ux-Designers born after the 1985
MATCH (n:`UX Designer`)
WITH n, split(n.birthdate,"-") AS bd
WHERE bd[2] > "1985"
RETURN n.name AS Name, n.surname AS Surname, bd[2] AS Birth ORDER BY Birth
