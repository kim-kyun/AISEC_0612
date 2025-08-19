let myname = "홍길동"
let myproject = " 인공지능 솔루션 적대적공격 보안을 위한 학습"

$(() => {
	$("#maintitle").text(`${myproject} [${myname}]`)
	$("title").text(`${myproject} [${myname}]`)
})
