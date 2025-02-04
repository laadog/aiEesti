# Automaatne hindamisaktide uuendaja

## Kasutamine
1. Lae alla [ollama](https://ollama.com/)
2. Lae alla keelemudel (soovituslikult deepSeek r1:8b)
`ollama pull deepseek-r1:8b`
3. Kasuta tööriista läbi käsurea
`python Interface.py [andmete kautst] [uuendatav dokument]`\
 näide:
`python Interface.py ../data/ '../hindamisakt.docx'`
3. Programm loob uued failid: UPDATED_failinime ja CHANGELOG_failinimi.txt

## Tööpõhimõte
1. Laeb kõik antud failid mällu ja jaotab paragraafideks.
2. Võrdleb originaalfailis olevaid paragraafe andmebaasis olevatetega, vastavalt LLM otsusele leiab parima kandidaadi.

## Kasutatud vahendid
* Python
* Docx dokumentide töötluseks
* ollama kohalikuks LLM serveriks, vaikimisi mudeliks on DeepSeek r1:8b, kuna arvestades suurust on jõudlus väga hea, samuti on paljud sammud `<think>` plokis, niiviisi on LLM otsust lihtsam tõlgendada.
* argparse CLI kasutajaliidese jaoks

## Puudused
* Üsnagi aeglane, peab käima läbi kõik paragraafid andmebaasis.
* Nõuab vormistatud faile, docx formaadis peaks olema sisu jaotunud lõikudeks

## Võimalikud edasiarendused
* Võimsam LLM, võimalusel teha tellimus API-le.
* Üksikute küsimuste asemel jaotada andmed sildistatud plokkidesse, ja need **RAG** (retrieval augmented generation) abil mudelile ette anda.
Tulemusena oleks uuendus märkimisväärselt kiirem ja eeldatavast ka täpsem, kuna mudelil on kogu aeg näha terve fail, mitte ainult üksik paragraaf.
* Praegune lahendus ei eelda mudelilt head eesti keele oskust, kuid suuremad mudelid võiksid ka vastavalt andmebaasile paragraafe ka ümber kirjutada.
