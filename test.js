/*
*******************************************************************************************************************
날일 : 초안일 (2021-12-22 水曜日)  |   수정일     : 2021-12-22 水曜日 수정자 : 조시욱
저자 : 조시욱                     |  진행 저자   : 수정 및 배포를 원하시면 진행 저자를 입력하시면됩니다! 저자만 살려주세요ㅠㅠ
제목 : simple js
내용 : 손이 많이 가는 특수기호를 포함한 값의 선언 또는 참조 구간을 최대한 줄였습니다.
버전 : 1.0.1
*******************************************************************************************************************
*/

// console.log 테스트 라인 ++ HOW-TO-USE : Ctrl + / 로 주석 해제 후 console.log('입력문구'); ++
// *******************************************************************************************************************
// console.log('안녕하세요 조시욱입니다.');
// *******************************************************************************************************************

//#region simple js [1] 자주 쓰이는 매크로 라인
// *******************************************************************************************************************
// 1) alert(알림) 매크로
// ex) Test_Alert('Test_Text')
function alert_Value(Test_Text) {
    if (Test_Text == null) {
        return alert('입력 텍스트가 누락되었습니다')
    }
    return alert(Test_Text)
}

// 2) insert(주입) 매크로
// ex) insert_Value('Address','insertvalue')
function insert_Value(Address, insertvalue) {
    Show_Insert_Val = $(Address).val(insertvalue)
    if (Address == null | insertvalue == null) {
        return alert('주소값 또는 밸류값이 누락되었습니다.')
    }
    return Show_Insert_Val;
}

// 3) append(추가) 매크로
// ex) Append_Value('Address','add_child')
function append_Value(Address, add_child) {
    Show_Append_Val = $(Address).append(add_child)
    if (Address == null | add_child == null) {
        return alert('주소값 또는 추가되어질 오브젝트가 누락되었습니다.')
    }
    return Show_Append_Val;
}

//#region  오브젝트 show and hide 매크로

const show_and_hide = {
// 4) show(보여주기) 매크로
// ex) show_Value('Address')
    show_Value: function (Address) {
        Show_Val = $(Address).show()
        if (Address == null) {
            return alert('보여질 주소가 누락되었습니다')
        }
        return Show_Val;
    },
// 5) hide(숨기기) 매크로
// ex) hide_Value('Address')
    hide_Value: function (Address) {
        Show_Hide_Val = $(Address).hide()
        if (Address == null) {
            return alert('숨길 주소가 누락되었습니다')
        }
        return Show_Hide_Val;
    }
}

//#endregion

//#region  리스트 push,clear 매크로

// 6) push(리스트에 아이템 추가) 매크로
// ex) push_Value('location','item')
function push_Value(location, item) {
    try {
        push_Val = location.push(item)
        if (item == null) {
            alert_Value('아이템 값이 누락되었습니다')
        } else {
            return push_Val;
        }
    } catch {
        alert_Value('아무런 값도 입력되지 않았습니다.')
    }
}

//#endregion

// *******************************************************************************************************************
//#endregion

//#region simple js [2] 사칙연산 매크로 라인
// *******************************************************************************************************************
const calulator = {
// 1) Summary(더하기) 매크로
// ex) Summary_Value(Param1,Param2, ..., ...)
    Summary_Value: function (...Param) {
        var sum_Result = 0;
        if (Param.length <= 1) {
            return alert('덧셈식은 두개의 값 이상이여야합니다.')
        }
        for (var i = 0; i < Param.length; i++) {
            sum_Result += Param[i]
        }
        return sum_Result;
    },
// 2) Multiply(곱하기) 매크로
// ex) Multiply_Value(Param1,Param2, ..., ...)
    Multiply_Value: function (...Param) {
        var Multiply_Result = 1;
        if (Param.length <= 1) {
            return alert('곱셈식은 두개의 값 이상이여야합니다.')
        }
        for (var i = 0; i < Param.length; i++) {
            Multiply_Result *= Param[i]
        }
        return Multiply_Result;
    },
// 3) Sqaured(거듭제곱) 매크로
// ex) squared_Value(Param1,Param2)
    squared_Value: function (Param1, Param2) {
        if (Param1 == 1)
        {
            return alert('거듭 제곱은 2부터 가능합니다.')
        }
        if (Param2 == null | Param1 == null)
        {
            return alert('밑 또는 지수가 누락되었습니다.')
        }
        if (Param1 * Param2 == 0) {
            return Param1;
        } else {
            return Param1 ** Param2;
        }
    }
}
// *******************************************************************************************************************
//#endregion