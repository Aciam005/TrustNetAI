**TrustNetAI – Sistem de Detectare a Phishing-ului bazat pe AI**

* **Descriere:** Aplicație web dezvoltată pentru identificarea automată a tentativelor de phishing prin analiza inteligentă a fluxului de e-mailuri.
* **Tehnologii:** Python, Flask, OpenAI API (GPT-3.5-Turbo), IMAP, HTML.
* **Funcționalități cheie:**
* Implementarea unui modul de conectare securizată la servere de e-mail (ex. Outlook/Office 365) utilizând protocolul IMAP pentru preluarea mesajelor în timp real.
* Integrarea modelelor de limbaj de mari dimensiuni (LLM) prin API-ul OpenAI pentru a evalua subiectul, expeditorul și conținutul e-mailurilor, generând un verdict de securitate și un scor de certitudine.
* Dezvoltarea unei interfețe web intuitive folosind framework-ul Flask, care permite declanșarea analizelor AI printr-o singură interacțiune.
* Procesarea structurilor de e-mail complexe (multipart), incluzând decodarea header-elor și gestionarea automată a atașamentelor prin salvarea acestora în directoare dedicate pentru analiză ulterioară.


* **Impact:** Automatizează trierea mesajelor suspecte, oferind un strat suplimentar de securitate cibernetică prin utilizarea procesării limbajului natural pentru detectarea indicatorilor de fraudă.
