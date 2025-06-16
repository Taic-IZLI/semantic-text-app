const sidebar = document.createElement('div');
sidebar.style.position = 'fixed';
sidebar.style.left = '-250px';
sidebar.style.top = '0';
sidebar.style.width = '250px';
sidebar.style.height = '100%';
sidebar.style.backgroundColor = '#000000aa';
sidebar.style.color = '#00ffcc';
sidebar.style.padding = '1em';
sidebar.style.transition = 'left 0.3s ease-in-out';
sidebar.innerHTML = `
  <h3>📘 Навигация</h3>
  <p>1. Введите тексты</p>
  <p>2. Нажмите "Сравнить"</p>
  <p>3. Смотрите результат</p>
`;

document.body.appendChild(sidebar);

document.body.addEventListener("mousemove", function (e) {
  if (e.clientX < 20) {
    sidebar.style.left = '0';
  } else if (e.clientX > 270) {
    sidebar.style.left = '-250px';
  }
});
