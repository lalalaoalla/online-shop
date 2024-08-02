for (let link of document.querySelectorAll('a[href^="#"]')) {  //берем все ссылки у которых путь начинается с #
	//то есть это мы ссылаемся на то, что находится на этой странице
	link.addEventListener('click', function (e) {// обозначаем, что данная функция срабатывает при нажатии на ссыллку
		e.preventDefault();                        //выключаем стандартную реакцию браузера(переход на другую страницу)
		let item = link.getAttribute('href');		//получаем путь(присваивает item нашу ссылку) 

		document.querySelector(item).scrollIntoView({   //сначала ищем нашу ссылку на странице
			//(то есть наше #contact превращается в contact)
			//потом делаем ее видимой
			block: "center",// по центру находится блок
			behavior: "smooth"// прокрутка плавная, а не мгновенная
		})
	})
}

//ПРИМЕНЯЕТСЯ В about.html cabinet.html cart.html catalogue.html index.html login.html product.html registration.html