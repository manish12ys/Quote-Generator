document.getElementById('generate-btn').addEventListener('click', async () => {
    const category = document.getElementById('category').value;
    const response = await fetch(`/quote?category=${category}`);
    const data = await response.json();
    document.getElementById('quote-text').innerText = data.text;
});

document.getElementById('copy-btn').addEventListener('click', () => {
    const quote = document.getElementById('quote-text').innerText;
    navigator.clipboard.writeText(quote);
    alert('Quote copied!');
});

document.getElementById('share-btn').addEventListener('click', () => {
    const quote = document.getElementById('quote-text').innerText;
    const url = `https://twitter.com/intent/tweet?text=${encodeURIComponent(quote)}`;
    window.open(url, '_blank');
});

document.getElementById('toggle-theme').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});
