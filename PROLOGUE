% Chatbot knowledge base
response(hi, 'Hello! How can I help you?').
response(hello, 'Hi there! What can I do for you?').
response(how_are_you, 'I am just a program, but I am doing fine!').
response(help, 'I can answer basic greetings and help questions.').
response(bye, 'Goodbye! Have a great day.').

% Process user input
chat :-
    write('You: '), read(Input),
    ( response(Input, Reply) ->
        format('Bot: ~w~n', [Reply]),
        (Input == bye -> true ; chat)
    ; write('Bot: Sorry, I do not understand.'), nl, chat ).
