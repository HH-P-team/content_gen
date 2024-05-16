from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Subject(Base):
    __tablename__ = 'subject'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    products: Mapped[list['Product']] = relationship(
        back_populates="subject", cascade="all, delete-orphan"
        )
    
    def __repr__(self) -> str:
        return f'Subject(id={self.id}, name={self.name})'
    

class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(100))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subject.id"))
    subject: Mapped['Subject'] = relationship(back_populates='products')
    posts: Mapped[list['Post']] = relationship(
        back_populates="product", cascade="all, delete-orphan"
        )

    def __repr__(self) -> str:
        return f'Product(id={self.id}, name={self.name})'


class Post(Base):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(1000))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    product: Mapped['Product'] = relationship(back_populates='posts')

    def __repr__(self) -> str:
        return f'Post(id={self.id}, name={self.name})'