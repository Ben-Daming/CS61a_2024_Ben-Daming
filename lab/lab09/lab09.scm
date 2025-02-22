(define (over-or-under num1 num2) 
        (cond ((< num1 num2) -1)
          ((= num1 num2) 0)
          (else 1)))

(define (make-adder num) 
  (lambda (inc) (+ num inc))
)


(define (composed f g) 
  (lambda (x) (f (g x)))
)

(define (repeat f n) 
  (if (= n 0)
    (lambda (x) x)
    (lambda (x) ((composed f (repeat f (- n 1))) x))
  )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (if (zero? (modulo (max a b) (min a b))) 
    (min a b)
    (gcd (min a b) (modulo (max a b) (min a b)))
  )
)
