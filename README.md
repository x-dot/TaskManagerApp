# Task Manager App

* **Ονοματεπώνυμο:** ΓΡΗΓΟΡΑΚΟΣ ΧΡΗΣΤΟΣ
* **Αριθμός Μητρώου:** Π2020146
* **Μάθημα:** Τεχνολογία Λογισμικού
* **Ημερομηνία:** Ιανουάριος 2026

---

## Περιγραφή Εργασίας
Στα πλαίσια της εργασίας αναπτύχθηκε ενα web task manager app. Η εφαρμογή επιτρέπει στον χρήστη να βλέπει, να προσθέτει, να ψαχνει και να διαγράφει tasks.

Η υλοποίηση έγινε με χρήση της γλώσσας **Python** και του πλαισίου **Flask**, ενώ η αποθήκευση των δεδομένων γίνεται σε αρχείο μορφής **JSON**. Η εφαρμογή είναι πλήρως containerized μέσω **Docker** και διαθέτει αυτοματοποιημένο έλεγχο (CI) μέσω **GitHub Actions**.

### Βασικά Χαρακτηριστικά
1.  **REST API:** Υλοποιήθηκαν τα endpoints:
    * `GET /tasks`: Επιστροφή όλων των task.
    * `POST /tasks`: Δημιουργία νεου task.
    * `GET /tasks/<id>` : Αναζήτηση task με ID.
    * `DELETE /tasks/<id>`: Διαγραφή task με ID.
2.  **Frontend:** Δημιουργία UI (HTML/JS) για εύκολη χρήση μέσω browser.
3.  **Persistence:** Μόνιμη αποθήκευση δεδομένων στο αρχείο `tasks.json` (ακόμα και μετά την επανεκκίνηση του Docker).
4.  **Unit Testing:** Συγγραφή ελέγχων με τη βιβλιοθήκη `pytest` για την διασφάλιση της ορθής λειτουργίας του API.
5.  **Docker:** Δημιουργία `Dockerfile` για την αυτόματη εγκατάσταση και εκτέλεση της εφαρμογής σε οποιοδήποτε περιβάλλον.
6.  **CI/CD:** Ρύθμιση GitHub Actions workflow (`ci.yml`) που τρέχει αυτόματα τα tests σε κάθε push ή pull request.

---

## Οδηγίες Εγκατάστασης & Εκτέλεσης (Docker)

### Build το Image
Στο τερματικό, μέσα στον φάκελο της εφαρμογής:
```bash
docker build -t task-manager-app .
```

### Για να τρέξει η εφαρμογή και να διατηρούνται τα δεδομένα στο tasks.json:
# Windows
```powershell
Windows(powershell): docker run -p 5000:5000 -v ${PWD}/tasks.json:/app/tasks.json task-manager-app
```
# Linux/maxOS 
```bash
docker run -p 5000:5000 -v "$(pwd)/tasks.json:/app/tasks.json" task-manager-app
```

---

Η εφαρμογή θα είναι προσβάσιμη στο 
```
http://localhost:5000
```

