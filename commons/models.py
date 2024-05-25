from datetime import datetime
from uuid import UUID

from sqlalchemy import Boolean, DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Mixin:
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime,
                                                  default=func.now(), onupdate=func.now())


class Subject(Base, Mixin):
    __tablename__ = 'subject'

    name: Mapped[str] = mapped_column(String(100))
    products: Mapped[list['Product']] = relationship(back_populates='subject',
                                                     lazy='selectin',
                                                     cascade='all, delete-orphan')
    image: Mapped['Image'] = relationship(back_populates='subject', 
                                          lazy='selectin',
                                          single_parent=True,
                                          cascade='all, delete-orphan')
    
    def __repr__(self) -> str:
        return f'Subject(id={self.id}, name={self.name})'
    

class Product(Base, Mixin):
    __tablename__ = 'product'

    name: Mapped[str] = mapped_column(String(100), nullable=True)
    description: Mapped[str] = mapped_column(String(100), nullable=True)
    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id'))
    subject: Mapped['Subject'] = relationship(back_populates='products')
    posts: Mapped[list['Post']] = relationship(back_populates='product',
                                               lazy='selectin',
                                               cascade='all, delete-orphan')
    image: Mapped['Image'] = relationship(back_populates='product',
                                          lazy='selectin',
                                          cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f'Product(id={self.id}, name={self.name})'


class Post(Base, Mixin):
    __tablename__ = 'post'

    description: Mapped[str] = mapped_column(String(10000), nullable=True)
    query: Mapped[str] = mapped_column(String(10000))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    product: Mapped['Product'] = relationship(back_populates='posts', lazy='selectin')
    image: Mapped['Image'] = relationship(back_populates='post',
                                          lazy='selectin',
                                          cascade='all, delete-orphan')

    def __repr__(self) -> str:
        return f'Post(id={self.id}, name={self.product.name}, query={self.query})'
    

class Image(Base, Mixin):
    __tablename__ = 'image'

    uuid: Mapped[UUID] = mapped_column(Uuid)
    subject_id: Mapped[int] = mapped_column(ForeignKey('subject.id'), nullable=True)
    subject: Mapped['Subject'] = relationship(back_populates='image',
                                              cascade='all, delete-orphan',
                                              single_parent=True)
    
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'), nullable=True)
    product: Mapped['Product'] = relationship(back_populates='image',
                                              cascade='all, delete-orphan',
                                              single_parent=True)
    
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=True)
    post: Mapped['Post'] = relationship(back_populates='image',
                                        cascade='all, delete-orphan',
                                        single_parent=True)
    
    in_progress: Mapped[bool] = mapped_column(Boolean, default=True, nullable=True)

    def __repr__(self) -> str:
        return f'Image(id={self.id})'
    

def get_model_from_tablename(tablename):
  for c in Base.registry._class_registry.data.values():
    if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
      return c