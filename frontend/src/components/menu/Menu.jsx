import './Menu.css';
import MenuButton from './MenuButton';

export default function Menu(props) {
    return (
        <div className="Menu">
            <MenuButton name='Категории' />
            <MenuButton name='Продукты' />
            <MenuButton name='Рекламные посты' />
        </div>
    );
}
