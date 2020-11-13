# Darbs grupā

## Darba process

- Izvēlieties 2 dažādus uzdevumus:
  - vienu uzdevumu risinājuma rakstīšanai
  - vienu uzdevumu testu rakstīšanai
- Paziņojiet saviem grupas biedriem Slack kanālā par izvēlētajiem uzdevumiem. Vienojieties, lai katram izvēlētajam uzdevumu kāds cits rakstītu testus, un katram testam būtu kāds, kas raksta risinājumu, piemēram:
  - Anna izvēlas uzdevumu A risināšanai un uzdevumu B testēšanai
  - Boriss izvēlas uzdevumu B risināšanai un uzdevumu C testēšanai
  - Dainis izvelas uzdevumu B risināšanai un uzdevumu A testēšanai
  - Zaiga izvēlas uzdevumu C risināšanai un uzdevumu A testēšanai
- Izveidojiet zaru ar savu vārdu
- Izveidojiet jaunu datni "src" mapē un rakstiet tajā risinājumu izvēlētajam uzdevumam. Veiciet "pull request" darbplūsmu:
  - lokali: git commit
  - lokāli: git push
  - github.com: create pull request
  - palūdziet, lai kāds cits github.com veic "merge pull request"
- Informējiet Slack kāds ir datnes nosaukums un jūsu izvelētais funkcijas nosaukums, lai testu rakstītāji var to pārbaudīt.
- Noskaidrojiet no kolēģiem kāds ir datnes un funkcijas nosaukums uzdevumam, kuram Jūs rakstīsiet testus.
- Izveidojiet jaunu datni "test" mapē un rakstiet tajā testus izvēlētajam uzdevumam. Veiciet "pull request" darbplūsmu, lai pievienotu testus kopīgajam repozitorijam.
- Lokāli pārejiet uz zaru "main" un veiciet git pull, lai saņemtu visu grupas darbu.

## Uzdevumi

### A. Drošs dalījums

    Funkcija akceptē divus argumentus - skaiļus a un b,
    aprēķina to dalījumu un atgriež to. Ja skaiļus dalīt nedrīkst,
    atgriež 0.

    Argumenti:
        a {int vai float} -- pirmais skaitlis
        b {int vai float} -- otrais skaitlis
    Atgriež:
        int vai float -- rezultāts

### B. Trijstūra laukums

    Funkcija akceptē divus argumentus - trisjtūra augstumu un pamatu,
    aprēķina trijstūra laukumu un atgriež to. Ja kāds no argumentiem ir mazāks vai vienāds ar 0, atgriež 0.
    Formula trijstūra laukuma aprēķināšanai ir augstums*pamats/2

    Argumenti:
        h {int vai float} -- trijstūra augstums
        p {int vai float} -- trijstūra pamats
    Atgriež:
        int vai float -- rezultāts

### C. Temperatūras pārveidošana C->K

    Funkcija akceptē vienu argumentu - temperatūru Celsija grādos,
    un atgriež temperatūru Kelvina grādos. Zemākā temperatūra
    Kelvina grādos var būt 0, tādēļ, ja aprēķinātā temperatūra ir
    zemāka, atgriež 0.

    Argumenti:
        t {int vai float} -- temperatūra Celsija grādos
    Atgriež:
        int vai float -- temperatūra Kelvina grādos

### D. Temperatūras pārveidošana F->C

    Funkcija akceptē vienu argumentu - temperatūru Fārenheita grādos,
    un atgriež temperatūru Celsija grādos. Zemākā temperatūra
    Celsija grādos var būt −273.15, tādēļ, ja aprēķinātā temperatūra ir zemāka, atgriež −273.15.

    Argumenti:
        t {int vai float} -- temperatūra Fārenheita grādos
    Atgriež:
        int vai float -- temperatūra Celsija grādos

### E. Kvadrātvienādojuma saknes

    Funkcija akceptē trīs argumentu - kvadrātvienādojuma 
    koeficientus a,b un c.
    Funcija atgriež masīvu ar saknēm vai None, ja sakņu nav.

    Argumenti:
        a {int vai float} -- koeficients a (pie x^2)
        b {int vai float} -- koeficients b (pie x)
        c {int vai float} -- koeficients c
    Atgriež:
        list [] -- vienādojuma saknes vai None
