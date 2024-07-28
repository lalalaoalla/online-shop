$(document).ready(function() {
    let position = 0//position - текущее положение слайдера, то есть в самом начале
    
    const slidesToShow = 1// количество элементов, которые видны одновременно
    const slidesToScroll = 1// количество элементов, передвигающихся за один раз
    
    const container = $(".slider-container")
    const track = $(".slider-track")
    const item = $(".slider-item")

    const btnprev = $(".slider-prev")
    const btnnext = $(".slider-next")

    const itemWidth = container.width() / slidesToShow // ширина одного слайда(ширина конт\кол-во эл)

    const movePosition = slidesToScroll * itemWidth// расстояние, на которое должен переместиться элемент

    const itemsCount = item.length// общее количество слайдов

    btnprev.click(function() {//при клике на кнопку назад
        position += movePosition// позиция увеличивается на расстояние, которое мы должны сдвинуть
        setPosition()//запоминаем позицию, на которую сдвинули
        checkBtns()//проверяем, нужно ли отключать кнопки вперед или назад
    })
    // то же самое только при клике на кнопку вперед
    btnnext.click(function() {
        position -= movePosition
        setPosition()
        checkBtns()
    })

    const setPosition = () => {
        track.css({// для track мы выполняем
            transform: `translateX(${position}px)`//какое-то css свойство
        })
    }

    const checkBtns = () => {
        btnprev.prop('disabled', position === 0)//отключаем кнопку назад если слайдер находится в начале
        btnnext.prop('disabled', position <= -(itemsCount - slidesToShow) * itemWidth)//отключаем в конце
    }
    checkBtns()//задаем начальное положение кнопок
})

//ИСПОЛЬЗУЕТСЯ В index.html