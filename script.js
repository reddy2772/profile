function contentShow() {
    const content = document.getElementById('addcontent');
    const button = document.getElementById('contentshow');

    if (content.style.display === 'none') {
        content.style.display = 'block';
        button.textContent = 'Show Less';

    } else {
        content.style.display = 'none';
        button.textContent = 'Show More'; 
    }

}

function regards() {
    alert('Thank you for your message!');
}
