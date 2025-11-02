document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('div.highlight').forEach(function(codeBlock) {
    var codeText = codeBlock.querySelector('pre > code').innerText;

    var button = document.createElement('button');
    button.className = 'copy-btn';
    button.type = 'button';
    button.innerText = 'Copy';

    button.setAttribute('data-clipboard-text', codeText);

    codeBlock.appendChild(button);
  });

  var clipboard = new ClipboardJS('.copy-btn');

  clipboard.on('success', function(e) {
    e.trigger.innerText = 'Copied!';
    setTimeout(function() {
      e.trigger.innerText = 'Copy';
    }, 2000);
    e.clearSelection();
  });

  clipboard.on('error', function(e) {
    e.trigger.innerText = 'Error';
  });
});