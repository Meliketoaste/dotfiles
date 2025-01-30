[
  (block)
  (struct_member)
  (enum_declaration)
  (union_declaration)
  (struct_declaration)
  (struct)
  (parameters)
  (tuple_type)
  (call_expression)
  (switch_case)
] @indent.begin

; hello(
((identifier) . (ERROR "(" @indent.begin))

[
  ")"
  "]"
] @indent.branch @indent.end

; Have to do all closing brackets separately because the one for switch statements shouldn't end.
(block "}" @indent.branch @indent.end)
(enum_declaration "}" @indent.branch @indent.end)
(union_declaration "}" @indent.branch @indent.end)
(struct_declaration "}" @indent.branch @indent.end)
(struct "}" @indent.branch @indent.end)

; Handle struct members with inline struct types
(struct_member
  (type (struct_type) @indent.begin
  (#set! "scope" "all") ; Force fresh indent context

; Special case for closing inline structs
(struct_member
  (type 
    (struct_type "}" @indent.end))
  (#set! "scope" "all"))

; Keep existing general struct rules
(struct_declaration "{" @indent.begin)
(struct_type "{" @indent.begin)
(struct_declaration "}" @indent.end)
(struct_type "}" @indent.end)

[
  (comment)
  (block_comment)
  (string)
  (ERROR)
] @indent.auto

;
; (type ; [56, 8] - [59, 2]
;   (struct_type ; [56, 8] - [59, 2]
;     (struct_member ; [57, 1] - [57, 7]
;       (identifier) ; [57, 1] - [57, 2]
;       (type ; [57, 4] - [57, 7]
;         (identifier))) ; [57, 4] - [57, 7]
;     (struct_member ; [58, 1] - [58, 7]
;       (identifier) ; [58, 1] - [58, 2]
;       (type ; [58, 4] - [58, 7]
;         (identifier))))) ; [58, 4] - [58, 7]
;
; (if_statement ; [74, 4] - [77, 5]
;   condition: (binary_expression ; [74, 7] - [74, 29]
;     left: (identifier) ; [74, 7] - [74, 21]
;     right: (boolean)) ; [74, 25] - [74, 29]
;   consequence: (block ; [74, 30] - [77, 5]
;     (member_expression ; [75, 8] - [75, 26]
;       (identifier) ; [75, 8] - [75, 11]
;       (call_expression ; [75, 12] - [75, 26]
;         function: (identifier) ; [75, 12] - [75, 19]
;         argument: (string ; [75, 20] - [75, 25]
;           (string_content)))))) ; [75, 21] - [75, 24]
