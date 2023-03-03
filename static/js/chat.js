$(document).ready(function() {
    $('#inputForm').submit(function(e) {
      e.preventDefault();
      $.ajax({
        type: 'POST',
        url: '/chat/',
        data: {
          'text': $('#textInput').val(),
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
          $('#textInput').val('');
          $('#chatBox').append('<div class="chat-bubble user-bubble">' + response.input_text + '</div>');
          $('#chatBox').append('<div class="chat-bubble chatbot-bubble">' + response.response_text + '</div>');
          $("#chatBox").scrollTop($("#chatBox")[0].scrollHeight);
        },
        error: function(xhr, errmsg, err) {
          console.log(xhr.status + ': ' + xhr.responseText);
        }
      });
    });
  });
  