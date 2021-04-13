# Domácí úkol č. 8
> **Upravujte pouze soubor `ukol_8_1.py`!**

## Načtení filmové databáze
Soubor `movie_rating.csv` obsahuje tabulární data o 13 řádcích a 10 sloupcích. Sloupce tabulky zahrnují název filmu, žánr a hodnocení
od 8 fanoušků v rozsahu 0–10. Pokud fanoušek film nehodnotil, je místo hodnocení uveden znak “x”. Tabulka může mít
např. tento formát: 

| Home Alone | Comedy | 7 |x|9|10|0|x|7|8|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**The Godfather**|**Drama**|**x**|**10**|**x**|**x**|**10**|**9**|**x**|**x**|

Prostudujte specifikace souborového formátu `*.csv` a zjistěte, jakým způsobem jsou data v souboru `movie_rating.csv` organizována. 

Ve funkci `load()` vytvořte program, který ze souboru načte veškerá data a uloží je do datové struktury typu `seznam` v následující (ilustrativní) formě:

```python
movie_data = [["Home Alone", "Comedy", ["7", "9", "10", "0", "7", "8"]],
              ["The Godfather", "Drama", ["10", "10", "9"]]]
```

Program musí být schopen zpracovat tabulku libovolných rozměrů, tedy s libovolným počtem řádků a libovolným počtem
hodnocení (sloupců 3 – n). Nejmenší možný rozměr tabulky je 1x3.

Pro snadné načtení `*.csv` souboru je vhodné importovat modul `csv`. Pro postupné načtení řádků v `*.csv` souboru pak
použijte příslušnou funkci s následujícími parametry:

```python
delimiter=";", quotechar="|"
```

Načtená data budou reprezentovat výstupní paramter funkce. Funkci zavolejte v řídící funkci `main()` (název souboru jí předejte
pomocí globální proměnné `FILE_NAME`) a výsledek vytiskněte.

### Dokumentační řetězce
Funkci doplňte o dokumentační řetězec s popisem účelu funkce a vstupních a výstupních parametrů.
