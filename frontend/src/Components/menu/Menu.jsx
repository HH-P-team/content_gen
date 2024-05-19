import './Menu.css';
import MenuButton from './MenuButton';

export default function Menu(props) {
    return (
        <div className="Menu">
            <MenuButton path={'/subjects'} name='Категории' />
            <MenuButton path={'/products'} name='Продукты' />
            <MenuButton path={'/posts'} name='Рекламные посты' />
            <MenuButton path={'/profile'} name='Профиль' />
            <MenuButton path={'/about'} name='О проекте' />
            <MenuButton path={'/help'} name='Помощь' />
        </div>
    );
}
