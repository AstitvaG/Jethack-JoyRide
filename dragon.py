import defs,rider
col_df='\x1b[38;2;33;160;8m'
col_db='\x1b[48;2;33;160;8m'
dragon_main = [
	[
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▘','',-1],

	],
	[
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','_','',-1],
		[col_df,'','_','',-1],
		[col_df,'','_','',-1],
		[col_df,'','◢','',-1],
		['[31m',col_db,'◢','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▄','',-1],
		[col_df,'','◣','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▗','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		['','',' ','',-1],
		['','',' ','',-1],

	],
	[
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▀','',-1],
		[col_df,'','▀','',-1],
		[col_df,'','▀','',-1],
		[col_df,'','▀','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▖','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▗','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		['','',' ','',-1],
		['','',' ','',-1],

	],
	[
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▗','',-1],
		[col_df,'','▛','',-1],
		[col_df,'','▀','',-1],
		[col_df,'','▀','',-1],
		[col_df,'','▘','',-1],
		[col_df,'','▝','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▖','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▘','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],

	],
	[
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▄','',-1],
		[col_df,'','▄','',-1],
		[col_df,'','▄','',-1],
		[col_df,'','▄','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▗','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▘','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],

	],
	[
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▗','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▘','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],

	],
	[
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▗','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▘','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▝','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▖','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▐','',-1],
		['','',' ','',-1],

	],
	[
		['','',' ','',-1],
		[col_df,'','▗','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▘','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▝','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▖','',-1],
		['','',' ','',-1],
		[col_df,'','▗','',-1],
		[col_df,col_db,'█','',1],
		['','',' ','',-1],

	],
	[
		[col_df,'','▗','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▘','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		['','',' ','',-1],
		[col_df,'','▝','',-1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,col_db,'█','',1],
		[col_df,'','▘','',-1],
		['','',' ','',-1],

	],
]

class Dragon(rider.Rider):
	def __init__(self):
		super().__init__(int(defs.columns)-len(dragon_main[0])-4,int(defs.rows)//2,dragon_main)
		self.dragon = dragon_main
		# self.xpos_left = int(defs.columns)-len(dragon_main[0])-4
		# self.ypos_top = int(defs.rows)//2
		# self.art_areax=range(self.xpos_left,self.xpos_left+len(dragon_main[0]))
		# self.art_areay=range(self.ypos_top,self.ypos_top+len(dragon_main))
	def move(self,chbuff,x=False,val=-1):
		if chbuff == 'w':
			self.ypos_top -= 4 if (val==-1) else val
			if self.ypos_top<0:
				self.ypos_top=0
		elif chbuff == 's':
			self.ypos_top += 2 if val==-1 else val
			if self.ypos_top>int(defs.rows)-1-len(dragon_main):
				self.ypos_top=int(defs.rows)-1-len(dragon_main)
		self.art_areax=range(self.xpos_left,self.xpos_left+len(self.dragon[0]))
		self.art_areay=range(self.ypos_top,self.ypos_top+len(self.dragon))
