(load "/home/chris/code/lisp/asdf")
(Load #P"/home/chris/quicklisp/setup.lisp")
(ql:quickload :split-sequence)

(defvar filename "/home/chris/code/eulerproject/data/p042_words.txt")

(defun convert (n)
    "convert the letter to it's numeric value"
    (- (char-code n) (char-code #\@)))

(defun get-num (v)
    "sum the letter values in a word"
    (let ((c 0))
        (loop for a across (subseq v 1 (- (length v) 1)) do
            (setf c (+ c (convert a))))
            (return-from get-num c)))

(defun is-triangle-num (i)
    (let ((n 0) (v 0))
        (loop for n from 1 while (< v i) do
            (setf v (* (/ n 2) (+ n 1)))
            (if (= v i) (return t)))))


(with-open-file (s filename)
    (let* ((len (file-length s))
          (data (make-string len)))
        (read-sequence data s)
        (setf vals (split-sequence:SPLIT-SEQUENCE #\, data)))
    (let ((found 0))
        (loop for word in vals do
            (setf num (get-num word))
            (if (is-triangle-num num) (incf found)))
        (print found)))
