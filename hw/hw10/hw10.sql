CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT b.child AS chil
  FROM dogs AS a,parents AS b 
  WHERE b.parent = a.name
  ORDER BY a.height DESC;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT a.name AS name,b.size AS size
  from dogs AS a,sizes AS b
  WHERE a.height>b.min and a.height<=b.max;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child AS first ,b.child AS second 
  from parents as a,parents as b
  where a.parent = b.parent and a.child<b.child;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT ('The two siblings, '||a.first||' and '||a.second||', have the same size: '||b.size) as sentence
  from siblings as a,size_of_dogs as b,size_of_dogs as c
  where a.first = b.name and a.second = c.name and b.size = c.size;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT a.fur as fur,(MAX(a.height)-MIN(a.height)) as height_range
  from dogs as a
  GROUP BY a.fur
  HAVING (AVG(a.height)*0.7)<MIN(a.height) and (AVG(a.height)*1.3)>MAX(a.height);