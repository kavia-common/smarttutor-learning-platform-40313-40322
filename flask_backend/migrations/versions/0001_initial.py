"""initial

Revision ID: 0001_initial
Revises:
Create Date: 2025-10-29 00:00:00.000000
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0001_initial'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('role', sa.String(length=32), nullable=False, server_default='student'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)

    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_courses_title', 'courses', ['title'], unique=False)

    op.create_table(
        'lessons',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id', ondelete='CASCADE'), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('video_url', sa.String(length=1024), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_lessons_course_id', 'lessons', ['course_id'], unique=False)

    op.create_table(
        'enrollments',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id', ondelete='CASCADE'), nullable=False),
        sa.Column('enrolled_at', sa.DateTime(), nullable=False),
        sa.UniqueConstraint('user_id', 'course_id', name='uq_enrollments_user_course')
    )
    op.create_index('ix_enrollments_user_id', 'enrollments', ['user_id'], unique=False)
    op.create_index('ix_enrollments_course_id', 'enrollments', ['course_id'], unique=False)

    op.create_table(
        'chat_messages',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id', ondelete='CASCADE'), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_chat_messages_course_id', 'chat_messages', ['course_id'], unique=False)
    op.create_index('ix_chat_messages_user_id', 'chat_messages', ['user_id'], unique=False)

    op.create_table(
        'whiteboard_sessions',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id', ondelete='CASCADE'), nullable=False),
        sa.Column('lesson_id', sa.Integer(), sa.ForeignKey('lessons.id', ondelete='SET NULL'), nullable=True),
        sa.Column('status', sa.String(length=32), nullable=False, server_default='active'),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_whiteboard_sessions_course_id', 'whiteboard_sessions', ['course_id'], unique=False)
    op.create_index('ix_whiteboard_sessions_lesson_id', 'whiteboard_sessions', ['lesson_id'], unique=False)

    op.create_table(
        'whiteboard_events',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('session_id', sa.Integer(), sa.ForeignKey('whiteboard_sessions.id', ondelete='CASCADE'), nullable=False),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('type', sa.Text(), nullable=False),
        sa.Column('payload', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_whiteboard_events_session_id', 'whiteboard_events', ['session_id'], unique=False)
    op.create_index('ix_whiteboard_events_user_id', 'whiteboard_events', ['user_id'], unique=False)

    op.create_table(
        'payments',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id', ondelete='CASCADE'), nullable=False),
        sa.Column('amount', sa.Numeric(10, 2), nullable=False),
        sa.Column('currency', sa.String(length=8), nullable=False, server_default='USD'),
        sa.Column('status', sa.String(length=32), nullable=False, server_default='succeeded'),
        sa.Column('provider', sa.String(length=64), nullable=True),
        sa.Column('reference', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_payments_user_id', 'payments', ['user_id'], unique=False)
    op.create_index('ix_payments_course_id', 'payments', ['course_id'], unique=False)

    op.create_table(
        'recommendations_cache',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('data', sa.JSON(), nullable=True),
        sa.Column('generated_at', sa.DateTime(), nullable=False),
        sa.Column('expires_at', sa.DateTime(), nullable=True),
    )
    op.create_index('ix_recommendations_cache_user_id', 'recommendations_cache', ['user_id'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_recommendations_cache_user_id', table_name='recommendations_cache')
    op.drop_table('recommendations_cache')

    op.drop_index('ix_payments_course_id', table_name='payments')
    op.drop_index('ix_payments_user_id', table_name='payments')
    op.drop_table('payments')

    op.drop_index('ix_whiteboard_events_user_id', table_name='whiteboard_events')
    op.drop_index('ix_whiteboard_events_session_id', table_name='whiteboard_events')
    op.drop_table('whiteboard_events')

    op.drop_index('ix_whiteboard_sessions_lesson_id', table_name='whiteboard_sessions')
    op.drop_index('ix_whiteboard_sessions_course_id', table_name='whiteboard_sessions')
    op.drop_table('whiteboard_sessions')

    op.drop_index('ix_chat_messages_user_id', table_name='chat_messages')
    op.drop_index('ix_chat_messages_course_id', table_name='chat_messages')
    op.drop_table('chat_messages')

    op.drop_index('ix_enrollments_course_id', table_name='enrollments')
    op.drop_index('ix_enrollments_user_id', table_name='enrollments')
    op.drop_table('enrollments')

    op.drop_index('ix_lessons_course_id', table_name='lessons')
    op.drop_table('lessons')

    op.drop_index('ix_courses_title', table_name='courses')
    op.drop_table('courses')

    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
