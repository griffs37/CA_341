insertBT(X,nil,tree(nil,X,nil)).
insertBT(X,tree(L,Y,R),T) :- Y>=X, insertBT(X,L,L1), T=tree(L1,Y,R).
insertBT(X,tree(L,Y,R),T) :- Y<X, insertBT(X,R,R1), T=tree(L,Y,R1).

searchBT(X,tree(_,X,_)):-!.
searchBT(X,tree(L,Y,_)):-Y>X,searchBT(X,L),!.
searchBT(X,tree(_,Y,R)):-Y<X,searchBT(X,R),!.

inorderBT(nil,[]).
inorderBT(tree(L,X,R),B) :- inorderBT(L,OL),inorderBT(R,OR),append([X],OR,A),append(OL,A,B).

preorderBT(nil,[]).
preorderBT(tree(L,X,R),[X|A]) :- preorderBT(L,OL),preorderBT(R,OR),append(OL,OR,A).

postorderBT(nil,[]).
postorderBT(tree(L,X,R),B) :- postorderBT(L,OL),postorderBT(R,OR),append(OR,[X],A),append(OL,A,B).

option(N) :- 
	write("Select an option:\n0. End program\n1. Create new empty tree\n2. Add num to current tree\n3. Search num in current tree\n4. Print inorder tree\n5. Print preorder tree\n6. Print postorder tree\n"),
	read(N),!.

choice(1,_,B):-B=nil.
choice(2,T,B):-
	write("Enter the number that you want to add"),nl,
	read(I),
	insertBT(I,T,B).
choice(3,T,T):-
	write("Enter the number that you want to search"),nl,
	read(I),
	search_result(I,T).
choice(4,T,T):-
	inorderBT(T,L),
	write(L),nl.
choice(5,T,T):-
	preorderBT(T,L),
	write(L),nl.
choice(6,T,T):-
	postorderBT(T,L),
	write(L),nl.

search_result(N,T):-searchBT(N,T),write("The number is in the BST"),nl.
search_result(N,T):-not(searchBT(N,T)),write("The number wasn't found"),nl.

main(T) :-
	option(N),
	N>=1,6>=N,
	choice(N,T,B),
	main(B).

main :- main(nil).