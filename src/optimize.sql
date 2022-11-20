create table stock_price like stock_price_sh;
insert table stock_price select * from stock_price_sh;
alter table stock_price add primary key (code, date);
alter table stock_price add index code (code);
inset into stock_price select * from stock_price_sz;

