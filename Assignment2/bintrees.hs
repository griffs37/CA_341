data BinTree a = Nil | Tree (BinTree a) a (BinTree a) deriving Show

insertBT :: (Ord a) => a -> BinTree a -> BinTree a
insertBT x Nil = Tree Nil x Nil
insertBT x (Tree left y right)
	| x<=y = Tree (insertBT x left) y right
	| otherwise = Tree left y (insertBT x right)

searchBT :: (Ord a) => a -> BinTree a -> Bool
searchBT x Nil = False
searchBT x (Tree left y right)
	| x==y = True
	| x<y = searchBT x left
	| x>y = searchBT y right

inorderBT :: BinTree a -> [a]
inorderBT Nil = []
inorderBT (Tree left x right) = inorderBT left ++ [x] ++ inorderBT right

preorderBT :: BinTree a -> [a]
preorderBT Nil = []
preorderBT (Tree left x right) = x : (preorderBT left ++ preorderBT right) 

postorderBT :: BinTree a -> [a]
postorderBT t = postorderBT' [] t
	where
		postorderBT' l Nil = l
		postorderBT' l (Tree left x right) = postorderBT' (postorderBT' (x:l) right) left

options :: IO Int
options = do
	putStr "Select an option:\n0. End program\n1. Create new empty tree\n2. Add integer to current tree\n3. Search integer in current tree\n4. Print inorder tree\n5. Print preorder tree\n6. Print postorder tree\n"
	l <- getLine
	return $ read l

input :: String -> IO Int
input s = do
	putStrLn $ "Enter the number that you want to "++s
	l <- getLine
	return $ read l

main' :: BinTree Int -> IO ()
main' b = do
	n <- options
	case n of
		0 -> return ()
		1 -> main' Nil
		2 -> do
			i <- input "add"
			main' $ insertBT i b
		3 -> do
			i <- input "search"
			if searchBT i b
				then do
					putStrLn "The number is in the BST"
					_ <- getLine
					main' b
				else do
					putStrLn "The number wasn't found"
					_ <- getLine
					main' b
		4 -> do
			putStrLn $ show $ inorderBT b
			_ <- getLine
			main' b
		5 -> do
			putStrLn $ show $ preorderBT b
			_ <- getLine
			main' b
		6 -> do
			putStrLn $ show $ postorderBT b
			_ <- getLine
			main' b
		_ -> do
			putStrLn "Invalid input"
			_ <- getLine
			main' b

main = main' Nil