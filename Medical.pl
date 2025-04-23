% Facts and rules for diagnosis
diagnose(flu) :- symptom(fever), symptom(cough), symptom(body_ache).
diagnose(cold) :- symptom(cough), symptom(sneezing), symptom(runny_nose).
diagnose(covid19) :- symptom(fever), symptom(cough), symptom(loss_of_taste).

% Ask user for symptoms
symptom(S) :- ask(S).

% Dynamic storage for answers
:- dynamic known/1.

ask(S) :-
    known(S), !.
ask(S) :-
    \+ known(S),
    format('Do you have ~w? (yes/no): ', [S]),
    read(Reply),
    (Reply == yes -> assertz(known(S)); fail).

% Entry point
start :-
    retractall(known(_)),
    diagnose(Disease),
    format('You might have ~w.~n', [Disease]), !.
start :-
    write('Sorry, diagnosis could not be made.'), nl.
