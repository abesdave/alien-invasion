Alien Invasion
==============

Mad​ aliens​ are​ about​ to​ invade​ the​ Earth, and you are tasked with simulating the iminent invasion.

You​ are​ given​ a map​ containing​ the​ names​ of​ cities​ in​ the​ non-existent​ world​ of X.​ 
The​ map​ is​ in​ a file,​ with​ one​ city​ per​ line.​ 
The​ city​ name​ is​ first, followed​ by​ 1-4​ directions​ (north,​ south,​ east,​ or​ west).​ 
Each​ one​ represents​ a road​ to​ another​ city​ that​ lies​ in​ that​ direction.
For​ example:

```
Foo​ north=Bar​ west=Baz​ south=Qu-ux
Bar​ south=Foo​ west=Bee
```
A single space separates the city and each pair,​ and​ the directions​ are​ separated​ from​ their​ respective​ cities​ with​ an​ equals​ (=)​ sign.

You​ should​ create​ N aliens,​ where​ N is​ specified​ as​ a command-line​ argument. These​ aliens​ start​ at​ random​ places​ on​ the​ map​ and​ wander​ around​ randomly, following​ links.​ At each​ iteration,​ the​ aliens​ can​ travel​ in​ any​ direction leading​ out​ of​ a city.​ 
In​ our​ example​ above,​ an​ alien​ that​ starts​ at​ Foo​ can​ go north​ to​ Bar,​ west​ to​ Baz,​ or​ south​ to​ Qu-ux.

When two aliens end up in the same place, they fight and, in the process, kill each other and destroy the city.​ 
When​ a city​ is​ destroyed,​ it​ is​ removed​ from the​ map,​ as​ are​ any​ roads​ that​ lead​ into​ or​ out​ of​ it. 
In​ our​ example​ above,​ if​ Bar​ were​ destroyed,​ the​ map​ would​ now​ be​:

```
Foo​ west=Baz​ south=Qu-ux
```

Once​ a city​ is​ destroyed,​ aliens​ can​ no​ longer​ travel​ to​ or​ through​ it.​ This may​ lead​ to​ aliens​ getting​ "trapped".

You​ should​ create​ a program​ that​ 
- Reads​​ the​ world​ map,​ 
- Creates​ N aliens,​
- Unleashes​ the aliens.​ 
- Run​ until​ all​ the​ aliens​ have​ been destroyed​ or​ each​ alien​ has​ moved​ at​ least​ 10,000​ times.​ 

When​ two​ aliens fight,​ print​ out​ a message​ like:

```bash
Bar has been destroyed by Alien 10 and Alien 34!
```

(If​ you​ want​ to​ give​ the aliens names,​ you​ may,​ but​ it​ is​ not​ required.)​ 

Once​ the program​ has​ finished,​ it​ should​ print​ out​ whatever​ is​ left​ of​ the​ world​ in​ the same​ format​ as​ the​ input​ file.

Feel​ free​ to​ make​ assumptions​ (for​ example,​ that​ the​ city​ names​ will​ never contain​ numeric​ characters),​ but​ please​ add​ comments​ or​ assertions​ describing
the​ assumptions​ you​ are​ making.

