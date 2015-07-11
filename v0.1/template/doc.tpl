<html>
	<head>
		<title>Felfeli Dictionary</title>
		<meta charset="UTF-8" />
		<link rel='stylesheet' href='/static/style.css' type='text/css' />
	</head>
	
	<body>
		<div class='dict'>
			<div calss='up'>
				<div class='search'>
					<form action="/dict" method="post">
						<input value="{{text}}" id="txtbox-style" type="text" name="words" size="20">
						<br/>
						<a href="/dict/help">?</a>
						<br/>
						<input id="btn-style" onmousemove="this.style.backgroundPosition='0px -33px';" onmouseout="this.style.backgroundPosition='0px 0px';" style="background-position: 0px 0px;" type="submit" value="ترجمه کن !">
					</form>
				</div>
			</div>
			
			<div class='down'>
			%if len(words)!=0:
				<br/><span id="result-info">{{len(words)}} مورد یافت شد.</span><br/>
			%end
			%for i in words:
				{{! '<br/>'}}
				<div class="item">
					<p class='word'><b><u><i>{{i[0]}}</i></u></b></p>
					<p class="definition">{{! i[1]}}</p>
				</div>
			%end
			</div>
		</div>
		<p id="felfeli">Felfeli Dictionary</p>
	</body>
</html>
