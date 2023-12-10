// Select all elements with the class "request-box"
const requestBoxes = document.querySelectorAll('.request-box');
// Select all elements with the class "image-container"
const galleryImages = document.querySelectorAll('.image-container');
// Select the expanded view element by its ID
const expandedView = document.getElementById('expanded-view');
// Select various elements inside the expanded view
const expandedImage = document.getElementById('expanded-image');
const expandedName = document.getElementById('expanded-name');
const expandedInfo = document.getElementById('expanded-info');
const closeButton = document.getElementById('close-button');

// Add click event listeners to each request box
requestBoxes.forEach(box => {
  box.addEventListener('click', () => {
    const personImage = box.querySelector('.person-image');
    const personName = box.querySelector('h2');
    const personBloodType = box.querySelector('.blood-type');

    expandedImage.src = personImage.src;
    expandedName.textContent = personName.textContent;
    expandedInfo.textContent = `Blood Type: ${personBloodType.textContent}`;

    expandedView.style.display = 'block';
  });
});

// Add click event listeners to each gallery image
galleryImages.forEach(image => {
  image.addEventListener('click', () => {
    const personId = image.querySelector('.overlay').getAttribute('data-person-id');
    const personInfoDiv = document.getElementById(personId);

    if (personInfoDiv) {
      const personName = personInfoDiv.querySelector('h2');
      const personInfo = personInfoDiv.querySelector('p');

      expandedImage.src = image.querySelector('img').src;
      expandedName.textContent = personName.textContent;
      expandedInfo.textContent = personInfo.textContent;

      expandedView.style.display = 'block';
    }
  });
});

// Add click event listener to the close button
closeButton.addEventListener('click', () => {
  expandedView.style.display = 'none';
});
