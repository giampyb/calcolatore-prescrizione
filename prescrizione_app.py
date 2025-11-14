<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calcolatore Prescrizione Reati</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { font-family: 'Inter', sans-serif; }
        /* Nasconde frecce input numero */
        input[type="number"]::-webkit-inner-spin-button,
        input[type="number"]::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }
        input[type="number"] { -moz-appearance: textfield; }
        
        .form-input, .form-select { @apply w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500; }
        .form-label { @apply block text-sm font-medium text-gray-700 mb-1; }
        .btn { @apply px-4 py-2 rounded-md font-semibold text-white shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2; }
        .btn-blue { @apply bg-blue-600 hover:bg-blue-700 focus:ring-blue-500; }
        .btn-red { @apply bg-red-600 hover:bg-red-700 focus:ring-red-500; }
        .card { @apply bg-white p-6 rounded-lg shadow-lg mb-6; }
        
        /* Colori richiesti: Arancio e Verde Chiaro */
        .result-box { @apply p-6 rounded-lg text-center text-gray-900; }
        .result-box-ordinaria { @apply bg-orange-200; } /* Arancio Chiaro */
        .result-box-massima { @apply bg-green-200; } /* Verde Chiaro */
        
        .result-box h3 { @apply text-lg font-semibold mb-2; }
        .result-box p { @apply text-3xl font-bold; }
        #log-container { display: none; @apply mt-4 p-4 bg-gray-50 border border-gray-200 rounded-md; }
        #log-container h4 { @apply font-semibold text-lg mb-2 text-gray-800; }
        #log-container ul { @apply list-disc list-inside space-y-1 text-gray-700; }
        .alert { @apply p-4 rounded-md mb-4; }
        .alert-blue { @apply bg-blue-100 border border-blue-300 text-blue-800; }
        .sospensione-item { @apply flex justify-between items-center p-2 bg-gray-100 rounded-md mb-2; }
        input[type=range] { @apply w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer; }
    </style>
</head>
<body class="bg-gray-100 p-4 md:p-8">
    <div class="max-w-4xl mx-auto">
        <div class="card">
            <h1 class="text-3xl font-bold text-center text-gray-800 mb-6">Calcolatore Prescrizione Reati</h1>

            <!-- Sezione Input Principali -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <!-- Colonna Pena -->
                <div>
                    <h2 class="text-xl font-semibold text-gray-700 mb-3 border-b pb-2">1. Pena Edittale (Art. 157 c.p.)</h2>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="pena-anni" class="form-label">Pena Massima Edittale (Anni)</label>
                            <input type="number" id="pena-anni" class="form-input" placeholder="Es. 6" value="6" min="0" max="30">
                        </div>
                        <div>
                            <label for="pena-mesi" class="form-label">Pena Massima Edittale (Mesi)</label>
                            <input type="number" id="pena-mesi" class="form-input" placeholder="Es. 0" value="0">
                        </div>
                    </div>
                    <!-- Cursore Anni -->
                    <div class="mt-4">
                        <label for="pena-slider" class="form-label">Cursore Anni (0-30)</label>
                        <input type="range" id="pena-slider" min="0" max="30" value="6" class="w-full">
                    </div>
                </div>
                <!-- Colonna Date -->
                <div>
                    <h2 class="text-xl font-semibold text-gray-700 mb-3 border-b pb-2">2. Date Rilevanti</h2>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="data-commissione" class="form-label">Data Commissione Reato</label>
                            <input type="text" id="data-commissione" class="form-input" placeholder="gg/MM/AAAA" value="01/01/2015">
                        </div>
                        <div>
                            <label for="data-interruzione" class="form-label">Ultima Interruzione (opz.)</label>
                            <input type="text" id="data-interruzione" class="form-input" placeholder="gg/MM/AAAA">
                        </div>
                    </div>
                </div>
            </div>

            <!-- Sezione Opzioni e Qualifiche -->
            <div class="mb-6">
                <h2 class="text-xl font-semibold text-gray-700 mb-3 border-b pb-2">3. Opzioni e Qualifiche</h2>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="space-y-4">
                        <div class="flex items-center">
                            <input id="reato-tentato" type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500">
                            <label for="reato-tentato" class="ml-2 block text-sm text-gray-900">Reato Tentato (Art. 56 c.p. - Riduzione 1/3)</label>
                        </div>
                        <div class="flex items-center">
                            <input id="raddoppio-termini" type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500">
                            <label for="raddoppio-termini" class="ml-2 block text-sm text-gray-900">Raddoppio Termini (es. Art. 157 c. 6)</label>
                        </div>
                    </div>
                    <div>
                        <label for="tipo-reato" class="form-label">Minimo Edittale (Art. 157 c. 1)</label>
                        <select id="tipo-reato" class="form-select">
                            <option value="6">Delitto (Minimo 6 anni)</option>
                            <option value="4">Contravvenzione (Minimo 4 anni)</option>
                        </select>
                    </div>
                    <div>
                        <label for="cap-interruzione" class="form-label">Cap Aumento per Interruzioni (Art. 161 c.p.)</label>
                        <select id="cap-interruzione" class="form-select">
                            <option value="1.25">Standard (+1/4)</option>
                            <option value="1.5">Recidiva Art. 99 c. 2, 4, 5 (+1/2)</option>
                            <option value="1.6666666667">Recidiva Art. 99 c. 6 (+2/3)</option>
                            <option value="2">Abitualità / Professionalità (Doppio)</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- Sezione Sospensioni -->
            <div class="mb-6">
                <h2 class="text-xl font-semibold text-gray-700 mb-3 border-b pb-2">4. Periodi di Sospensione (Art. 159 c.p.)</h2>
                
                <div class="bg-blue-50 p-4 rounded-md border border-blue-200 mb-4">
                    <h3 class="font-semibold text-blue-800 mb-2">Sospensioni Automatiche</h3>
                    <div class="flex items-center">
                        <input id="sospensione-covid" type="checkbox" class="h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500">
                        <label for="sospensione-covid" class="ml-2 block text-sm text-gray-900">Includi Sospensione COVID "generica" (64 giorni - D.L. 18/2020)</label>
                    </div>
                    <div id="alert-orlando" class="alert alert-blue mt-3" style="display: none;">
                        <span class="font-bold">Regime "Orlando" Applicato:</span> Reato commesso nel periodo 03/08/2017 - 31/12/2019. L'app aggiunge automaticamente 1.5 anni (548 giorni) di sospensione.
                    </div>
                </div>

                <h3 class="font-semibold text-gray-800 mb-2">Aggiungi periodi manuali</h3>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                    <div>
                        <label for="sospensione-start" class="form-label">Data Inizio Sospensione</label>
                        <input type="text" id="sospensione-start" class="form-input" placeholder="gg/MM/AAAA">
                    </div>
                    <div>
                        <label for="sospensione-end" class="form-label">Data Fine Sospensione</label>
                        <input type="text" id="sospensione-end" class="form-input" placeholder="gg/MM/AAAA">
                    </div>
                    <div class="self-end">
                        <button id="btn-aggiungi-sospensione" class="btn btn-blue w-full">Aggiungi Periodo</button>
                    </div>
                </div>
                <div id="sospensioni-list" class="space-y-2"></div>
            </div>

            <!-- Bottone Calcola -->
            <div class="text-center mb-6">
                <button id="btn-calcola" class="btn btn-blue btn-lg text-xl px-8 py-3">Calcola Prescrizione</button>
            </div>

            <!-- Sezione Risultati -->
            <div id="risultati-container" class="space-y-4" style="display: none;">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Colore Arancio Chiaro -->
                    <div class="result-box result-box-ordinaria">
                        <h3>Prescrizione Ordinaria</h3>
                        <p id="data-prescrizione-ordinaria">--/--/----</p>
                        <span class="text-sm">(Calcolata da ultima interruzione, se presente)</span>
                    </div>
                    <!-- Colore Verde Chiaro -->
                    <div class="result-box result-box-massima">
                        <h3>Prescrizione Massima (Art. 161 c.p.)</h3>
                        <p id="data-prescrizione-massima">--/--/----</p>
                        <span class="text-sm">(Calcolata da data commissione reato)</span>
                    </div>
                </div>
                
                <div class="bg-gray-100 p-4 rounded-md border">
                    <h4 class="font-semibold text-gray-700 mb-2">Note Aggiuntive:</h4>
                    <ul class="list-disc list-inside text-sm text-gray-600 space-y-1">
                        <li>I termini minimi di 6 (delitti) o 4 (contravvenzioni) anni sono applicati automaticamente.</li>
                        <li>Sosp. "Orlando" (L. 103/2017): Per reati commessi nel periodo 03/08/2017 - 31/12/2019 l'app applica automaticamente 1.5 anni di sospensione (548 giorni).</li>
                        <li>Il calcolo della sospensione manuale NON include il giorno finale (es. 10/01 a 11/01 = 1 giorno).</li>
                    </ul>
                </div>

                <div class="text-center">
                    <button id="btn-mostra-log" class="text-blue-600 hover:underline">Mostra passaggi dettagliati</button>
                </div>
                <div id="log-container">
                    <h4>Log Dettagliato del Calcolo</h4>
                    <ul id="log-list"></ul>
                </div>
            </div>
        </div>
        
        <!-- Disclaimer Aggiunto -->
        <footer class="text-center mt-4 mb-6">
            <p class="text-sm text-gray-500">App realizzata dal dr. Giampiero Borraccia con Gemini AI</p>
        </footer>
    </div>

<script>
// Funzioni Utility per Date
function parseDate(str) {
    const parts = str.split('/');
    if (parts.length === 3) {
        // new Date(anno, mese - 1, giorno)
        return new Date(parts[2], parts[1] - 1, parts[0]);
    }
    return null;
}
function formatDate(date) {
    if (!date) return "--/--/----";
    const d = date.getDate().toString().padStart(2, '0');
    const m = (date.getMonth() + 1).toString().padStart(2, '0');
    const y = date.getFullYear();
    return `${d}/${m}/${y}`;
}
function addMonths(date, months) {
    const d = new Date(date);
    d.setMonth(d.getMonth() + months);
    return d;
}
function addDays(date, days) {
    const d = new Date(date);
    d.setDate(d.getDate() + days);
    return d;
}

// Funzione Aggiungi Sospensione
document.getElementById('btn-aggiungi-sospensione').addEventListener('click', () => {
    const startInput = document.getElementById('sospensione-start');
    const endInput = document.getElementById('sospensione-end');
    const list = document.getElementById('sospensioni-list');
    const startDate = parseDate(startInput.value);
    const endDate = parseDate(endInput.value);

    if (startInput.value && endInput.value && startDate && endDate && endDate > startDate) {
        const item = document.createElement('div');
        item.className = 'sospensione-item';
        item.dataset.start = startInput.value;
        item.dataset.end = endInput.value;
        item.innerHTML = `<span>Dal ${startInput.value} al ${endInput.value}</span>
                          <button class="btn btn-red btn-sm py-1 px-2" onclick="this.parentElement.remove()">Rimuovi</button>`;
        list.appendChild(item);
        startInput.value = '';
        endInput.value = '';
    } else {
        // Sostituiamo l'alert con un messaggio non bloccante
        console.error("Date di sospensione non valide o fine non successiva all'inizio.");
        // Potremmo aggiungere un piccolo box di errore sull'UI
    }
});

// Bottone Mostra/Nascondi Log
document.getElementById('btn-mostra-log').addEventListener('click', () => {
    const logContainer = document.getElementById('log-container');
    logContainer.style.display = logContainer.style.display === 'none' ? 'block' : 'none';
});

// Funzione Principale di Calcolo
document.getElementById('btn-calcola').addEventListener('click', calcolaPrescrizione);

function calcolaPrescrizione() {
    let logHtml = "";

    // --- PASSO 1: Acquisizione Input Base ---
    const penaAnni = parseInt(document.getElementById('pena-anni').value) || 0;
    const penaMesiInput = parseInt(document.getElementById('pena-mesi').value) || 0;
    let penaBaseMesi = (penaAnni * 12) + penaMesiInput;
    logHtml += `<li><b>Passo 1: Pena Edittale Base</b> -> ${penaAnni} anni e ${penaMesiInput} mesi = <b>${penaBaseMesi} mesi</b></li>`;

    const dataCommissione = parseDate(document.getElementById('data-commissione').value);
    const dataInterruzione = parseDate(document.getElementById('data-interruzione').value);
    if (!dataCommissione) { 
        console.error("Data commissione reato non valida o mancante.");
        return; // Sostituisce l'alert
    }

    const capInterruzione = parseFloat(document.getElementById('cap-interruzione').value);
    const tipoReatoMinimo = parseInt(document.getElementById('tipo-reato').value) * 12;

    // --- PASSO 2: Aumento per Aggravanti Effetto Speciale (Cass. 3391/2015) ---
    let aumentoEffettoSpecialeMesi = 0;
    let descAggravante = "";
    if (capInterruzione === 1.5) {
        aumentoEffettoSpecialeMesi = Math.ceil(penaBaseMesi * 0.5);
        descAggravante = "Recidiva +1/2";
    } else if (capInterruzione > 1.6 && capInterruzione < 1.7) {
        aumentoEffettoSpecialeMesi = Math.ceil(penaBaseMesi * (2/3));
        descAggravante = "Recidiva +2/3";
    } else if (capInterruzione === 2) {
        aumentoEffettoSpecialeMesi = penaBaseMesi;
        descAggravante = "Abitualità (Doppio)";
    }

    if (aumentoEffettoSpecialeMesi > 0) {
        penaBaseMesi += aumentoEffettoSpecialeMesi;
        logHtml += `<li><b>Passo 2: Aum. Agg. Eff. Speciale (Cass. 3391/2015)</b> -> ${descAggravante} (+${aumentoEffettoSpecialeMesi} mesi). Nuova pena base: <b>${penaBaseMesi} mesi</b></li>`;
    } else {
        logHtml += `<li><b>Passo 2: Aum. Agg. Eff. Speciale</b> -> Nessuno.</li>`;
    }

    // --- PASSO 3: Reato Tentato ---
    if (document.getElementById('reato-tentato').checked) {
        const riduzione = Math.ceil(penaBaseMesi / 3);
        penaBaseMesi -= riduzione;
        logHtml += `<li><b>Passo 3: Reato Tentato</b> -> Riduzione 1/3 (-${riduzione} mesi). Nuova pena base: <b>${penaBaseMesi} mesi</b></li>`;
    } else {
        logHtml += `<li><b>Passo 3: Reato Tentato</b> -> No.</li>`;
    }

    // --- PASSO 4: Applicazione Minimi Edittali (Art. 157 c. 1) ---
    let termineOrdinarioMesi = penaBaseMesi;
    if (termineOrdinarioMesi < tipoReatoMinimo) {
        termineOrdinarioMesi = tipoReatoMinimo;
        logHtml += `<li><b>Passo 4: Minimo Edittale</b> -> Pena inferiore al minimo (${tipoReatoMinimo} mesi). Termine portato a <b>${termineOrdinarioMesi} mesi</b></li>`;
    } else {
        logHtml += `<li><b>Passo 4: Minimo Edittale</b> -> Pena superiore al minimo. Termine ordinario: <b>${termineOrdinarioMesi} mesi</b></li>`;
    }

    // --- PASSO 5: Raddoppio Termini ---
    if (document.getElementById('raddoppio-termini').checked) {
        termineOrdinarioMesi *= 2;
        logHtml += `<li><b>Passo 5: Raddoppio Termini</b> -> Termine raddoppiato: <b>${termineOrdinarioMesi} mesi</b></li>`;
    } else {
        logHtml += `<li><b>Passo 5: Raddoppio Termini</b> -> No.</li>`;
    }
    
    // --- PASSO 6: Calcolo Sospensioni (Automatiche) ---
    let sospensioniTotaliGiorni = 0;
    if (document.getElementById('sospensione-covid').checked) {
        sospensioniTotaliGiorni += 64;
        logHtml += `<li><b>Passo 6.1: Sospensioni Auto</b> -> COVID D.L. 18/2020: <b>+64 giorni</b></li>`;
    }
    const dataOrlandoStart = new Date(2017, 7, 3); // 3 Agosto 2017
    const dataOrlandoEnd = new Date(2019, 11, 31); // 31 Dicembre 2019
    const alertOrlando = document.getElementById('alert-orlando');
    if (dataCommissione >= dataOrlandoStart && dataCommissione <= dataOrlandoEnd) {
        sospensioniTotaliGiorni += 548; // 1.5 anni
        logHtml += `<li><b>Passo 6.2: Sospensioni Auto</b> -> Regime Orlando (L. 103/2017): <b>+548 giorni</b></li>`;
        alertOrlando.style.display = 'block';
    } else {
        alertOrlando.style.display = 'none';
    }

    // --- PASSO 7: Calcolo Sospensioni (Manuali) ---
    let sospensioniManualiGiorni = 0;
    Array.from(document.getElementById('sospensioni-list').children).forEach(item => {
        const start = parseDate(item.dataset.start);
        const end = parseDate(item.dataset.end);
        if (start && end && end > start) {
            const diffTime = Math.abs(end.getTime() - start.getTime());
            // CORREZIONE: calcolo che non include giorno finale
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
            sospensioniManualiGiorni += diffDays;
            logHtml += `<li><b>Passo 7: Sosp. Manuale</b> -> ${item.dataset.start} - ${item.dataset.end}: <b>${diffDays} giorni</b></li>`;
        }
    });
    
    if (sospensioniManualiGiorni > 0) logHtml += `<li><b>Passo 7.1: Totale Sosp. Manuali</b> -> <b>${sospensioniManualiGiorni} giorni</b></li>`;
    else logHtml += `<li><b>Passo 7: Sosp. Manuali</b> -> Nessuna.</li>`;
    
    sospensioniTotaliGiorni += sospensioniManualiGiorni;
    logHtml += `<li class="font-bold text-blue-700"><b>--- Totale Giorni Sospensione: ${sospensioniTotaliGiorni} giorni ---</b></li>`;

    // --- PASSO 8: Calcolo Data Prescrizione ORDINARIA ---
    const dataRiferimentoOrdinaria = dataInterruzione || dataCommissione;
    let dataOrdinaria = addMonths(dataRiferimentoOrdinaria, termineOrdinarioMesi);
    dataOrdinaria = addDays(dataOrdinaria, sospensioniTotaliGiorni);
    document.getElementById('data-prescrizione-ordinaria').textContent = formatDate(dataOrdinaria);
    logHtml += `<li><b>Passo 8: Data Prescrizione Ordinaria</b> -> (Base: ${formatDate(dataRiferimentoOrdinaria)}) + ${termineOrdinarioMesi} mesi + ${sospensioniTotaliGiorni} giorni = <b>${formatDate(dataOrdinaria)}</b></li>`;

    // --- PASSO 9: Calcolo Data Prescrizione MASSIMA ---
    let termineMassimoMesi = Math.ceil(termineOrdinarioMesi * capInterruzione);
    logHtml += `<li><b>Passo 9.1: Termine Massimo (Art. 161)</b> -> ${termineOrdinarioMesi} mesi * ${capInterruzione.toFixed(2)} (cap) = <b>${termineMassimoMesi} mesi</b></li>`;

    let dataMassima = addMonths(dataCommissione, termineMassimoMesi);
    dataMassima = addDays(dataMassima, sospensioniTotaliGiorni);
    document.getElementById('data-prescrizione-massima').textContent = formatDate(dataMassima);
    logHtml += `<li class="font-bold text-red-700"><b>Passo 9.2: Data Prescrizione Massima</b> -> (Base: ${formatDate(dataCommissione)}) + ${termineMassimoMesi} mesi + ${sospensioniTotaliGiorni} giorni = <b>${formatDate(dataMassima)}</b></li>`;

    // Mostra risultati
    document.getElementById('log-list').innerHTML = logHtml;
    document.getElementById('risultati-container').style.display = 'block';
}

// Sincronizzazione Slider e Campo Anni
const penaAnniInput = document.getElementById('pena-anni');
const penaSlider = document.getElementById('pena-slider');

penaSlider.addEventListener('input', (e) => {
    penaAnniInput.value = e.target.value;
});
penaAnniInput.addEventListener('input', (e) => {
    let value = parseInt(e.target.value);
    if (isNaN(value)) value = 0;
    if (value > 30) value = 30;
    if (value < 0) value = 0;
    penaSlider.value = value;
    // Aggiorna anche il valore nel campo se corretto
    e.target.value = value; 
});
</script>
</body>
</html>