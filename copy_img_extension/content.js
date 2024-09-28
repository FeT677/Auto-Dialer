function observePhoneNumber() {
  const observer = new MutationObserver((mutations, observer) => {
    const phoneImage = document.querySelector('[data-marker="phone-popup/phone-image"]');
    
    if (phoneImage) {
      observer.disconnect();
      
      const imageType = phoneImage.src.split(';')[0].split(':')[1];
      if (imageType !== 'image/png') {
        console.warn("Телефон не в формате PNG");
      }

      const base64String = phoneImage.src.split(",")[1];
      const byteCharacters = atob(base64String);
      const byteNumbers = new Array(byteCharacters.length);
      for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
      }
      const byteArray = new Uint8Array(byteNumbers);
      const blob = new Blob([byteArray], { type: 'image/png' });

      copyToClipboard(blob);
    } else {
      console.warn("PNG с номером не найдено");
    }
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
}

function copyToClipboard(blob) {
  const item = new ClipboardItem({ "image/png": blob });
  navigator.clipboard.write([item]).then(() => {
    showNotification("Скопировано в буфер обмена");
  }).catch(err => {
    console.error("Ошибка копирования PNG: ", err);
  });
}

function showNotification(message) {
  // Создаём элемент уведомления
  const notification = document.createElement("div");
  notification.style.position = "fixed";
  notification.style.top = "15%";
  notification.style.left = "50%";
  notification.style.transform = "translate(-50%, -50%)";
  notification.style.padding = "15px 30px";
  notification.style.backgroundColor = "#4CAF50";
  notification.style.color = "white";
  notification.style.fontSize = "20px";
  notification.style.borderRadius = "10px";
  notification.style.boxShadow = "0px 4px 8px rgba(0, 0, 0, 0.1)";
  notification.style.zIndex = "10000";
  notification.textContent = message;

  document.body.appendChild(notification);

  setTimeout(() => {
    notification.remove();
  }, 3000);
}

// Запускаем скрипт сразу без ожидания загрузки страницы
observePhoneNumber();
